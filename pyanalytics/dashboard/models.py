from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse  # Used to generate URLs by reversing the URL patterns


class Report(models.Model):
    """
    Model representing an Analytics Report
    """
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=200)
    viewId = models.IntegerField(help_text="Enter the View ID for your analytics website")

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.name + ": " + str(self.viewId)

    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of the model.
        """
        return reverse('report-detail', args=[str(self.id)])
