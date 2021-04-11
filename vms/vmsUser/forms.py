from django import forms
from .models import Requisition, JOUR_PURPOSE


class RequisitionForm(forms.ModelForm):
    jour_purpose = forms.ChoiceField(required=True, label='Enter the Journey Purpose', choices=JOUR_PURPOSE,)
    jour_date = forms.DateField(required=True, label='Enter the Journey Date',
                                widget=forms.TextInput(attrs={'class': 'form-control'}))
    vcl_type = forms.CharField(required=True, label='Enter the Vehicle Type', max_length=200,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    destination = forms.CharField(required=True, label='Enter the Destination', max_length=200,
                                  widget=forms.TextInput(attrs={'class': 'form-control'}))
    departr_time = forms.TimeField(required=True, label='Enter the Departure Time',
                                   widget=forms.TextInput(attrs={'class': 'form-control'}))
    rtrn_time = forms.TimeField(required=True, label='Enter the Return Time',
                                widget=forms.TextInput(attrs={'class': 'form-control'}))
    jour_details = forms.CharField(label='Enter the more details about Journey', max_length=200,
                                   widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Requisition
        fields = ('jour_purpose', 'jour_date', 'vcl_type', 'destination', 'departr_time', 'rtrn_time',
                  'jour_details')
