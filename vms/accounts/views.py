# from django.http import request
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import CustomUserCreationForm, LoginForm
from django.views.generic import CreateView, FormView

from .models import NewUser


def homePage(request):
    return render(request, 'accounts/index.html')


def noticePage(request):
    return render(request, 'accounts/notice.html')


class SignUpView(CreateView):
    model = NewUser
    form_class = CustomUserCreationForm
    success_url = '/'
    template_name = 'accounts/register.html'


class LoginView(FormView):
    form_class = LoginForm
    success_url = 'vmsUser:user_home'

    def form_valid(self, form):
        request = self.request
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have been logged in")
            return redirect('user_home')
        else:
            messages.error(request, "Error logging in - please try again")
            return redirect('login')

    template_name = 'accounts/login.html'


def logoutUser(request):
    logout(request)
    messages.success(request, "You have been logged out")
    return redirect('homePage')
