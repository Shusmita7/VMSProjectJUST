from django.contrib.auth.forms import UserCreationForm, UserChangeForm, ReadOnlyPasswordHashField
from django import forms
from .models import NewUser


class UserAdminCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = NewUser
        fields = ('username', 'email', 'full_name', 'dept_sec', 'designation', 'contact_no')

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = super(UserAdminCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserAdminChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = NewUser
        fields = (
            'username', 'email', 'full_name', 'dept_sec', 'designation', 'contact_no', 'password', 'active', 'admin')

    def clean_password(self):
        return self.initial["password"]


class LoginForm(forms.Form):
    email = forms.EmailField(label='Email')
    password = forms.CharField(widget=forms.PasswordInput)

class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(label="Enter your Username", max_length=100,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    full_name = forms.CharField(help_text="", label="Enter your Full Name", max_length=150,
                                widget=forms.TextInput(attrs={'class': 'form-control'}))
    dept_sec = forms.CharField(help_text="", label="Enter your Department or Section", max_length=100,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    designation = forms.CharField(help_text="", label="Enter your Designation", max_length=100,
                                  widget=forms.TextInput(attrs={'class': 'form-control'}))
    contact_no = forms.CharField(help_text="", label="Enter your Contact Number", max_length=11,
                                 widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta(UserCreationForm.Meta):
        model = NewUser
        fields = ('username', 'email', 'full_name', 'dept_sec', 'designation', 'contact_no', 'password1', 'password2')


def __init__(self, *args, **kwargs):
    super(CustomUserCreationForm, self).__init__(*args, **kwargs)

    self.fields['email'].widget.attrs['class'] = 'form-control'
    self.fields['email'].widget.attrs['placeholder'] = ''
    self.fields['email'].help_text = ""

    self.fields['password1'].widget.attrs['class'] = 'form-control'
    self.fields['password1'].widget.attrs['placeholder'] = 'aaaa'
    self.fields['password1'].label = "Enter your Password"
    self.fields['password1'].help_text = ""

    self.fields['password2'].widget.attrs['class'] = 'form-control'
    self.fields['password2'].widget.attrs['placeholder'] = ''
    self.fields['password2'].label = "Confirm Your Password"
    self.fields['password2'].help_text = ""


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = NewUser
        fields = UserChangeForm.Meta.fields

# class SignUpForms(UserCreationForm):
#     username = forms.CharField(label="Enter your Username", max_length=100,
#                                widget=forms.TextInput(attrs={'class': 'form-control'}))
#     email = forms.EmailField(label="Enter your Email Address", max_length=100,
#                              widget=forms.TextInput(attrs={'class': 'form-control'}))
#     full_name = forms.CharField(help_text="", label="Enter your Full Name", max_length=150,
#                                 widget=forms.TextInput(attrs={'class': 'form-control'}))
#     dept_sec = forms.CharField(help_text="", label="Enter your Last Name", max_length=100,
#                                widget=forms.TextInput(attrs={'class': 'form-control'}))
#     designation = forms.CharField(help_text="", label="Enter your Last Name", max_length=100,
#                                   widget=forms.TextInput(attrs={'class': 'form-control'}))
#     contact_no = forms.CharField(help_text="", label="Enter your Last Name", max_length=11,
#                                  widget=forms.TextInput(attrs={'class': 'form-control'}))
#
#     class Meta:
#         model = NewUser
#         fields = ('username', 'email', 'full_name', 'dept_sec', 'designation', 'contact_no', 'password1', 'password2')
#
#     def __init__(self, *args, **kwargs):
#         super(SignUpForms, self).__init__(*args, **kwargs)
#
#         self.fields['username'].widget.attrs['class'] = 'form-control'
#         self.fields['username'].widget.attrs['placeholder'] = ''
#         self.fields['username'].help_text = ""
#
#         self.fields['password1'].widget.attrs['class'] = 'form-control'
#         self.fields['password1'].widget.attrs['placeholder'] = ''
#         self.fields['password1'].label = "Enter your Password"
#         self.fields['password1'].help_text = ""
#
#         self.fields['password2'].widget.attrs['class'] = 'form-control'
#         self.fields['password2'].widget.attrs['placeholder'] = ''
#         self.fields['password2'].label = "Confirm Your Password"
#         self.fields['password2'].help_text = ""
