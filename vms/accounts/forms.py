from django.contrib.auth.forms import UserCreationForm, UserChangeForm, ReadOnlyPasswordHashField
from django import forms
from .models import User


class UserAdminCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('codename', 'email', 'full_name', 'dept_sec', 'designation', 'contact_no')

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
        model = User
        fields = (
            'codename', 'email', 'full_name', 'dept_sec', 'designation', 'contact_no', 'password',)

    def clean_password(self):
        return self.initial["password"]


class LoginForm(forms.Form):
    email = forms.EmailField(label='Email')
    password = forms.CharField(widget=forms.PasswordInput)


# class LoginForm(AuthenticationForm):
#     username = forms.CharField(label='Email')
#     # email = forms.EmailField(label='Email')
#     # password = forms.CharField(widget=forms.PasswordInput)


class CustomUserCreationForm(UserCreationForm):
    codename = forms.CharField(required=True, label="Enter your Username", max_length=100,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True, label="Enter your Email Address", max_length=100,
                             widget=forms.TextInput(attrs={'class': 'form-control'}))
    full_name = forms.CharField(required=True, help_text="", label="Enter your Full Name", max_length=150,
                                widget=forms.TextInput(attrs={'class': 'form-control'}))
    dept_sec = forms.CharField(required=True, help_text="", label="Enter your Department or Section", max_length=100,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    designation = forms.CharField(required=True, help_text="", label="Enter your Designation", max_length=100,
                                  widget=forms.TextInput(attrs={'class': 'form-control'}))
    contact_no = forms.CharField(required=True, help_text="", label="Enter your Contact Number", max_length=11,
                                 widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('codename', 'email', 'full_name', 'dept_sec', 'designation', 'contact_no', 'password1', 'password2')


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = UserChangeForm.Meta.fields


class RegisterForm(forms.ModelForm):
    """
    The default
    """

    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['codename', 'email', 'full_name', 'dept_sec', 'designation', 'contact_no',]

    def clean_email(self):
        """
        Verify email is available.
        """
        email = self.cleaned_data.get('email')
        qs = User.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError("email is taken")
        return email

    # def clean(self):
    #     """
    #     Verify both passwords match.
    #     """
    #     cleaned_data = super().clean()
    #     password = cleaned_data.get("password")
    #     password_2 = cleaned_data.get("password_2")
    #     if password is not None and password != password_2:
    #         self.add_error("password_2", "Your passwords must match")
    #     return cleaned_data

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user
