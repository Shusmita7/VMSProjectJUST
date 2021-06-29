# from django.http import request
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate, views as auth_views
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CustomUserCreationForm, LoginForm, RegisterForm
from django.views.generic import CreateView, FormView
from django.utils.decorators import method_decorator

from .models import User


# from .decorators import unauthenticated_user


def homePage(request):
    return render(request, 'accounts/accountshome.html')


def noticePage(request):
    return render(request, 'accounts/accountsnotice.html')


# @method_decorator(unauthenticated_user, name='dispatch')
class SignUpView(CreateView):
    model = User
    form_class = RegisterForm
    success_url = 'login'
    template_name = 'accounts/register.html'

    def form_valid(self, form):
        request = self.request
        formsave = form.save()
        codename = form.cleaned_data.get('codename')
        group = Group.objects.get(name='guser')
        formsave.groups.add(group)
        messages.success(request, "You have successfully registered..." + codename)
        return redirect('login')


# @method_decorator(unauthenticated_user, name='dispatch')
class LoginView(FormView):
    form_class = LoginForm
    success_url = 'Home'
    template_name = 'accounts/login.html'

    def form_valid(self, form):
        request = self.request
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have been logged in")
            return redirect('Home')
        else:
            messages.error(request, "Error logging in - please try again")
            return redirect('login')


@login_required(login_url='login')
def logoutUser(request):
    logout(request)
    messages.success(request, "You have been logged out")
    return redirect('homePage')
