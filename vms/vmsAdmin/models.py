from django.db import models

 # Create your models here.

class Vehicles(models.Model):
    vcl_name = models.CharField(verbose_name='Vehicle Name', max_length=200, blank=True, null=True)
    vcl_number = models.CharField(verbose_name='Vehicle ID', max_length=50, blank=True, null=True, unique=True)
    vcl_type = models.CharField(verbose_name='Vehicle Category', max_length=200, blank=True, null=True)
    costperkm = models.IntegerField(verbose_name='Cost per km', null=True, blank=True)
    costperhr = models.IntegerField(verbose_name='Cost per hour', null=True, blank=True)
    mileage = models.IntegerField(verbose_name='Mileage', null=True, blank=True)
    vcl_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.vcl_name

class Drivers(models.Model):
    drvr_number = models.CharField(verbose_name='Driver ID', max_length=50, blank=True, null=True)
    drvr_name = models.CharField(verbose_name='Driver Name', max_length=200, blank=True, null=True)
    drvr_vcl = models.OneToOneField(Vehicles, on_delete=models.CASCADE)
    drvr_contact_no = models.CharField(verbose_name="Driver Contact Number", max_length=20, null=True, blank=True)
    drvr_email = models.EmailField(verbose_name='Driver Email Address', blank=True, null=True)

    def __str__(self):
        return self.drvr_name