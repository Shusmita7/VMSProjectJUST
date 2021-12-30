from django import forms

from .models import LogBook


class LogbookForm(forms.ModelForm):
    startingkm = forms.DecimalField(required=True, label='Enter starting value...')
    endingkm = forms.DecimalField(required=True, label='Enter ending value...')
    startingfuel = forms.DecimalField(required=True, label='Enter starting fuel...')
    suppliedfuel = forms.DecimalField(required=True, label='Enter supplied fuel...')
    endingfuel = forms.DecimalField(required=True, label='Enter ending fuel...')

    class Meta:
        model = LogBook
        fields = ('startingkm', 'endingkm', 'startingfuel', 'endingfuel', 'suppliedfuel')