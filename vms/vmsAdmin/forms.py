from django import forms
from .models import Vehicle, Driver


class VehicleForm(forms.ModelForm):
    vcl_name = forms.CharField(required=True, label='Enter the Vehicle Name', max_length=200,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    vcl_number = forms.IntegerField(required=True, label='Enter the Vehicle ID',
                                    widget=forms.TextInput(attrs={'class': 'form-control'}))
    vcl_type = forms.CharField(required=True, label='Enter the vehicle Category', max_length=200,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    costprkm = forms.IntegerField(required=True, label='Enter the Cost/km',
                                  widget=forms.TextInput(attrs={'class': 'form-control'}))
    costprhr = forms.IntegerField(required=True, label='Enter the Cost/hr',
                                  widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Vehicle
        fields = ('vcl_name', 'vcl_number', 'vcl_type', 'costprkm', 'costprhr')


class DriverForm(forms.ModelForm):
    drvr_name = forms.CharField(required=True, label='Enter the Driver Name', max_length=200,
                                widget=forms.TextInput(attrs={'class': 'form-control'}))
    drvr_number = forms.CharField(required=True, label='Enter the Driver ID',
                                     widget=forms.TextInput(attrs={'class': 'form-control'}))
    drvr_contact_no = forms.CharField(required=True, label='Enter Phone Number of Driver',
                                         widget=forms.TextInput(attrs={'class': 'form-control'}))
    drvr_email = forms.EmailField(label='Enter Email Address of Driver',
                                  widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Driver
        fields = ('drvr_name', 'drvr_number', 'drvr_vcl', 'drvr_contact_no', 'drvr_email')
