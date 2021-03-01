from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages


def home(request):
    return render(request, 'core/index.html')


def notice(request):
    return render(request, 'core/notice.html')


def loginUser(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have been logged in")
            return redirect('home')
        else:
            messages.error(request, "Error logging in - please try again")
            return redirect('login')
    else:
        return render(request, 'core/login.html')


def registerUser(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "You have successfully registered....")
            return redirect('home')
    else:
        form = UserCreationForm()

    context = {'form': form}
    return render(request, 'core/register.html', context)


def logoutUser(request):
    logout(request)
    messages.success(request, "You have been logged out")
    return redirect('home')
