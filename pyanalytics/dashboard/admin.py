from django.contrib import admin

# Register your models here. ksun, foobar123
from .models import Report
# admin.site.register(Report)

# Define the admin class
class ReportAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'viewId')

# Register the admin class with the associated model
admin.site.register(Report, ReportAdmin)
