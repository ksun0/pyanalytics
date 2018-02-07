from django.shortcuts import render
"""Analytics Reporting API V4."""
from apiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials

# Create your views here.
def index(request):
    """
    View function for home page of site.
    """
    analytics = initialize_analyticsreporting()
    response = get_report(analytics)
    r = get_response(response)
    r = r.split('\n')
    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'index.html',
        context={'response':r},
    )


SCOPES = ['https://www.googleapis.com/auth/analytics.readonly']
SERVICE_ACCOUNT_EMAIL = 'ksun-349@pyanalytics-193319.iam.gserviceaccount.com'
KEY_FILE_LOCATION = 'service_account.json'
VIEW_ID = '157537579'

def initialize_analyticsreporting():
    """Initializes an Analytics Reporting API V4 service object.
    Returns: An authorized Analytics Reporting API V4 service object.
    """
    credentials = ServiceAccountCredentials.from_json_keyfile_name(KEY_FILE_LOCATION, SCOPES)
    # Build the service object.
    analytics = build('analyticsreporting', 'v4', credentials=credentials)
    return analytics

def get_report(analytics):
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
