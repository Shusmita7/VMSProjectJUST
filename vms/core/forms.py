from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class SignUpForms(UserCreationForm):
    email = forms.EmailField(label="Enter your Email Address", widget=forms.TextInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(help_text="", label="Enter your First Name", max_length=100,
                                 widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(help_text="", label="Enter your Last Name", max_length=100,
                                widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(SignUpForms, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = ''
        self.fields['username'].label = "Enter your User Name"
        self.fields['username'].help_text = ""

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = ''
        self.fields['password1'].label = "Enter your Password"
        self.fields['password1'].help_text = ""

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = ''
        self.fields['password2'].label = "Confirm Your Password"
        self.fields['password2'].help_text = ""
