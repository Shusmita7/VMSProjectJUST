# from django.http import request
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import Group
from django.contrib import messages
from .forms import CustomUserCreationForm, LoginForm
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
    form_class = CustomUserCreationForm
    success_url = 'login'

    def form_valid(self, form):
        request = self.request
        form.save()
        # group = Group.objects.get(name='admin')
        # user.groups.add(group)
        messages.success(request, "You have successfully registered...")

    template_name = 'accounts/register.html'


# @method_decorator(unauthenticated_user, name='dispatch')
class LoginView(FormView):
    form_class = LoginForm
    success_url = 'vmsUser:Home'

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

    template_name = 'accounts/login.html'


def logoutUser(request):
    logout(request)
    messages.success(request, "You have been logged out")
    return redirect('homePage')


