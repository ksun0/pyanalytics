from django.shortcuts import render
from .models import Report
import json

"""Analytics Reporting API V4."""
from apiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials


# Create your views here.
def index(request):
    """
    View function for home page of site.
    """
    # Number of visits to this view, as counted in the session variable.
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'index.html',
        context={'num_visits': num_visits},
    )


from django.views import generic  # class based generic views


class ReportListView(generic.ListView):
    model = Report
    context_object_name = 'report_list'  # your own list of reports as a template variable
    template_name = 'report_list.html'  # Template name/location

    def get_queryset(self):
        return Report.objects.all()  # Get all reports

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super(ReportListView, self).get_context_data(**kwargs)
        # Create any data and add it to the context
        context['some_data'] = 'This is just some data'
        return context


class ReportDetailView(generic.DetailView):
    model = Report
    template_name = 'report_detail.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super(ReportDetailView, self).get_context_data(**kwargs)
        # Create any data and add it to the context
        VIEW_ID = self.object.viewId
        analytics = initialize_analytics_reporting()
        response = get_report(analytics, str(VIEW_ID))
        r = get_response(response)
        r = r.split('\n')
        context['response'] = r
        return context


# Instructions available at: https://developers.google.com/analytics/devguides/reporting/core/v4/quickstart/service-py
SCOPES = ['https://www.googleapis.com/auth/analytics.readonly']
KEY_FILE_LOCATION = 'service_account.json'
with open('service_account.json') as json_data:
    d = json.load(json_data)
    SERVICE_ACCOUNT_EMAIL = d['client_email']


def initialize_analytics_reporting():
    """Initializes an Analytics Reporting API V4 service object.
    Returns: An authorized Analytics Reporting API V4 service object.
    """
    credentials = ServiceAccountCredentials.from_json_keyfile_name(KEY_FILE_LOCATION, SCOPES)
    # Build the service object.
    analytics = build('analyticsreporting', 'v4', credentials=credentials)
    return analytics


def get_report(analytics, VIEW_ID):
    """Queries the Analytics Reporting API V4.
    Args: analytics: An authorized Analytics Reporting API V4 service object.
    Returns: The Analytics Reporting API V4 response.
    """
    return analytics.reports().batchGet(
        body={
            'reportRequests': [
                {
                    'viewId': VIEW_ID,
                    'dateRanges': [{'startDate': '7daysAgo', 'endDate': 'today'}],
                    'metrics': [{'expression': 'ga:sessions'}],
                    'dimensions': [{'name': 'ga:country'}]
                }]
        }
    ).execute()


def get_response(response):
    """Parses and prints the Analytics Reporting API V4 response.
    Args: response: An Analytics Reporting API V4 response.
    """
    r = ""
    for report in response.get('reports', []):
        columnHeader = report.get('columnHeader', {})
        dimensionHeaders = columnHeader.get('dimensions', [])
        metricHeaders = columnHeader.get('metricHeader', {}).get('metricHeaderEntries', [])

        for row in report.get('data', {}).get('rows', []):
            dimensions = row.get('dimensions', [])
            dateRangeValues = row.get('metrics', [])

            for header, dimension in zip(dimensionHeaders, dimensions):
                r += (header + ': ' + dimension + '\n')

            for i, values in enumerate(dateRangeValues):
                r += ('Date range: ' + str(i) + '\n')
                for metricHeader, value in zip(metricHeaders, values.get('values')):
                    r += (metricHeader.get('name') + ': ' + value + '\n')
    return r
