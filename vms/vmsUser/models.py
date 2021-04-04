from django.db import models

# Create your models here.

class Requisitionforms(models.Model):
    aplctn_date = models.DateTimeField(verbose_name='Date', null=True, blank=True)
    user_name = models.CharField(verbose_name='User Name', max_length=200, blank=True, null=True)
    designation = models.CharField(verbose_name='Designation', max_length=100, blank = True)
    department = models.CharField(verbose_name='Department', max_length=100, blank=True, null=True)
    jour_purpose = models.CharField(verbose_name='Journey Purpose', max_length=100, blank=True, null=True)
    jour_date = models.DateTimeField(verbose_name='Journey Date', blank=True, null=True)
    vcl_type = models.CharField(verbose_name='Vehicle Type', max_length=100, blank=True, null=True)
    destination = models.CharField(verbose_name='Destination', max_length=200, blank=True, null=True)
    deprtr_time = models.TimeField(verbose_name='Departure Time', blank=True, null=True)
    rtrn_time = models.TimeField(verbose_name='Return Time', blank=True, null=True) 
    jour_details = models.CharField(verbose_name='Journey Details', max_length=400, blank=True, null=True)

    def __str__(self):
        return self.user_name