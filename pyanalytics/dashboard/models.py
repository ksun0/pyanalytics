from django.db import models
from django.urls import reverse #Used to generate URLs by reversing the URL patterns

# Create your models here.
class Report(models.Model):
    """
    Model representing an Analytics Report
    """
    name = models.CharField(max_length=200)
    viewId = models.IntegerField(help_text="Enter the View ID for your analytics website")

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.name + ": " + str(self.viewId)

    # def get_absolute_url(self):
    #     """
    #     Returns the url to access a particular instance of the model.
    #     """
    #     return reverse('report', args=[str(self.viewId)])
