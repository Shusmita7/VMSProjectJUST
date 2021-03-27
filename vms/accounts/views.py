# from django.http import request
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import CustomUserCreationForm, LoginForm
from django.views.generic import CreateView, FormView

from .models import User, user_type


def homePage(request):
    return render(request, 'accounts/index.html')


def noticePage(request):
    return render(request, 'accounts/notice.html')


# class SignUpView(CreateView):
#     model = User
#     form_class = CustomUserCreationForm
#     success_url = '/'
#     template_name = 'accounts/register.html'
#
#
# class LoginView(FormView):
#     form_class = LoginForm
#     success_url = 'vmsUser:user_home'
#
#     def form_valid(self, form):
#         request = self.request
#         email = form.cleaned_data.get('email')
#         password = form.cleaned_data.get('password')
#         user = authenticate(request, email=email, password=password)
#         if user is not None:
#             login(request, user)
#             messages.success(request, "You have been logged in")
#             return redirect('user_home')
#         else:
#             messages.error(request, "Error logging in - please try again")
#             return redirect('login')
#
#     template_name = 'accounts/login.html'


def logoutUser(request):
    logout(request)
    messages.success(request, "You have been logged out")
    return redirect('homePage')


def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        full_name = request.POST.get('full_name')
        dept_sec = request.POST.get('dept_sec')
        designation = request.POST.get('designation')
        contact_no = request.POST.get('contact_no')
        password = request.POST.get('password')
        teacher = request.POST.get('teacher')
        chairman = request.POST.get('chairman')
        vadmin = request.POST.get('vadmin')
        vsubadmin = request.POST.get('vsubadmin')
        accountant = request.POST.get('accountant')

        user = User.objects.create_user(
            username=username,
            email=email,
            full_name=full_name,
            dept_sec=dept_sec,
            designation=designation,
            contact_no=contact_no,
        )
        user.set_password(password)
        user.save()

        usert = None
        if teacher:
            usert = user_type(user=user, is_teacher=True)
        elif chairman:
            usert = user_type(user=user, is_chairman=True)
        elif vadmin:
            usert = user_type(user=user, is_vadmin=True)
        elif vsubadmin:
            usert = user_type(user=user, is_vsubadmin=True)
        elif accountant:
            usert = user_type(user=user, is_accountant=True)

        usert.save()
        # Successfully registered. Redirect to homepage
        return redirect('homePage')
    return render(request, 'accounts/register.html')


def loginPage(request):
    if request.method == 'POST':
        email = request.POST.get('email')  # Get email value from form
        password = request.POST.get('password')  # Get password value from form
        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            type_obj = user_type.objects.get(user=user)
            if user.is_authenticated and type_obj.is_teacher:
                return redirect('user_home')
            elif user.is_authenticated and type_obj.is_chairman:
                return redirect('user_home')
            elif user.is_authenticated and type_obj.is_vadmin:
                return redirect('admin_home')
            elif user.is_authenticated and type_obj.is_vsubadmin:
                return redirect('sub_home')
            elif user.is_authenticated and type_obj.is_accountant:
                return redirect('acc_home')
        else:
            messages.error(request, "Error logging in - please try again")
            return redirect('home')

    return render(request, 'accounts/login.html')


def teacherhome(request):
    if request.user.is_authenticated and user_type.objects.get(user=request.user).is_teacher:
        return render(request, 'user_home')
    elif request.user.is_authenticated and user_type.objects.get(user=request.user).is_chairman:
        return redirect('user_home')
    elif request.user.is_authenticated and user_type.objects.get(user=request.user).is_vadmin:
        return redirect('admin_home')
    elif request.user.is_authenticated and user_type.objects.get(user=request.user).is_vsubadmin:
        return redirect('sub_home')
    elif request.user.is_authenticated and user_type.objects.get(user=request.user).is_accountant:
        return redirect('acc_home')
    else:
        return redirect('login')


def chairmanhome(request):
    if request.user.is_authenticated and user_type.objects.get(user=request.user).is_chairman:
        return redirect('user_home')
    elif request.user.is_authenticated and user_type.objects.get(user=request.user).is_teacher:
        return render(request, 'user_home')
    elif request.user.is_authenticated and user_type.objects.get(user=request.user).is_vadmin:
        return redirect('admin_home')
    elif request.user.is_authenticated and user_type.objects.get(user=request.user).is_vsubadmin:
        return redirect('sub_home')
    elif request.user.is_authenticated and user_type.objects.get(user=request.user).is_accountant:
        return redirect('acc_home')
    else:
        return redirect('home')


def adminhome(request):
    if request.user.is_authenticated and user_type.objects.get(user=request.user).is_vadmin:
        return redirect('admin_home')
    elif request.user.is_authenticated and user_type.objects.get(user=request.user).is_chairman:
        return redirect('user_home')
    elif request.user.is_authenticated and user_type.objects.get(user=request.user).is_teacher:
        return render(request, 'user_home')
    elif request.user.is_authenticated and user_type.objects.get(user=request.user).is_vsubadmin:
        return redirect('sub_home')
    elif request.user.is_authenticated and user_type.objects.get(user=request.user).is_accountant:
        return redirect('acc_home')
    else:
        return redirect('home')


def vsubadminhome(request):
    if request.user.is_authenticated and user_type.objects.get(user=request.user).is_vsubadmin:
        return redirect('sub_home')
    elif request.user.is_authenticated and user_type.objects.get(user=request.user).is_chairman:
        return redirect('user_home')
    elif request.user.is_authenticated and user_type.objects.get(user=request.user).is_teacher:
        return render(request, 'user_home')
    elif request.user.is_authenticated and user_type.objects.get(user=request.user).is_vadmin:
        return redirect('admin_home')
    elif request.user.is_authenticated and user_type.objects.get(user=request.user).is_accountant:
        return redirect('acc_home')
    else:
        return redirect('home')


def accountanthome(request):
    if request.user.is_authenticated and user_type.objects.get(user=request.user).is_accountant:
        return redirect('acc_home')
    elif request.user.is_authenticated and user_type.objects.get(user=request.user).is_chairman:
        return redirect('user_home')
    elif request.user.is_authenticated and user_type.objects.get(user=request.user).is_teacher:
        return render(request, 'user_home')
    elif request.user.is_authenticated and user_type.objects.get(user=request.user).is_vadmin:
        return redirect('admin_home')
    elif request.user.is_authenticated and user_type.objects.get(user=request.user).is_vsubadmin:
        return redirect('sub_home')
    else:
        return redirect('home')


