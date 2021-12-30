from django import forms
from .models import Vehicles, Drivers, VEHICLE_TYPE


class VehicleForm(forms.ModelForm):
    vcl_name = forms.CharField(required=True, label='Enter the Vehicle Name', max_length=200,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    vcl_number = forms.CharField(required=True, label='Enter the Vehicle ID',
                                 widget=forms.TextInput(attrs={'class': 'form-control'}))
    vcl_type = forms.ChoiceField(required=True, choices=VEHICLE_TYPE, label='Enter the vehicle Category', )
    costprkm = forms.DecimalField(required=True, label='Enter the Cost/km')
    costprhr = forms.DecimalField(required=True, label='Enter the Cost/hr')

    class Meta:
        model = Vehicles
        fields = ('vcl_name', 'vcl_number', 'vcl_type', 'costprkm', 'costprhr')


class DriverForm(forms.ModelForm):
    drvr_name = forms.CharField(required=True, label='Enter the Driver Name', max_length=200,
                                widget=forms.TextInput(attrs={'class': 'form-control'}))
    drvr_number = forms.CharField(required=True, label='Enter the Driver ID',
                                  widget=forms.TextInput(attrs={'class': 'form-control'}))
    drvr_type = forms.ModelChoiceField(required=True, label='Select Vehicle for the Driver',
                                       queryset=Vehicles.objects.all(),
                                       to_field_name='vcl_name',
                                       empty_label="Select vehicle")
    drvr_contact_no = forms.CharField(required=True, label='Enter Phone Number of Driver',
                                      widget=forms.TextInput(attrs={'class': 'form-control'}))
    drvr_email = forms.EmailField(label='Enter Email Address of Driver',
                                  widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Drivers
        fields = ('drvr_name', 'drvr_number', 'drvr_type', 'drvr_contact_no', 'drvr_email')
#widget=forms.NumberInput(attrs={'class': 'form-control'})