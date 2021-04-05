from django import forms
from .models import Requisition


class RequisitionForm(forms.ModelForm):
    aplctn_date = forms.DateTimeField(required=True, label='Enter Date',
                                      widget=forms.TextInput(attrs={'class': 'form-control'}))
    # user_name = forms.CharField(required=True, label='Enter Your Name', max_length=200,
    #                             widget=forms.TextInput(attrs={'class': 'form-control'}))
    designation = forms.CharField(required=True, label='Enter your Designation', max_length=200,
                                  widget=forms.TextInput(attrs={'class': 'form-control'}))
    department = forms.CharField(required=True, label='Enter your Department Name', max_length=200,
                                 widget=forms.TextInput(attrs={'class': 'form-control'}))
    jour_purpose = forms.CharField(required=True, label='Enter the Journey Purpose', max_length=200,
                                   widget=forms.TextInput(attrs={'class': 'form-control'}))
    jour_date = forms.DateTimeField(required=True, label='Enter the Journey Date',
                                    widget=forms.TextInput(attrs={'class': 'form-control'}))
    vcl_type = forms.CharField(required=True, label='Enter the Vehicle Type', max_length=200,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    destination = forms.CharField(required=True, label='Enter the Destination', max_length=200,
                                  widget=forms.TextInput(attrs={'class': 'form-control'}))
    departr_time = forms.TimeField(required=True, label='Enter the Departure Time',
                                   widget=forms.TextInput(attrs={'class': 'form-control'}))
    rtrn_time = forms.TimeField(required=True, label='Enter the Return Time',
                                widget=forms.TextInput(attrs={'class': 'form-control'}))
    jour_details = forms.CharField(required=True, label='Enter the more details about Journey', max_length=200,
                                   widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Requisition
        fields = (
        'aplctn_date', 'user_name', 'designation', 'department', 'jour_purpose', 'jour_date', 'vcl_type', 'destination',
        'departr_time', 'rtrn_time', 'jour_details')
