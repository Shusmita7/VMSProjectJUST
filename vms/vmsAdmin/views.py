from django.shortcuts import render, redirect
from django.views.generic import CreateView, FormView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.utils.decorators import method_decorator
# import sys
#
# sys.path.append("..")

from .forms import DriverForm, VehicleForm
from .models import Drivers, Vehicles
# from ..accounts.decorators import admin_only
from vmsUser.models import Requisition


# def admin_only(view_func):
#     def wrapper_func(request, *args, **kwargs):
#         group = None
#         if request.user.groups.exists():
#             group = request.user.groups.all()[0].name
#         if group == 'chairman':
#             return redirect('Home')
#         if group == 'teacher':
#             return redirect('Home')
#         if group == 'subadmin':
#             return redirect('SubadminHome')
#         if group == 'accountant':
#             return redirect('acc_home')
#         if group == 'admin':
#             return view_func(request, *args, **kwargs)
#
#     return wrapper_func


@login_required(login_url='login')
# @admin_only
def adminHome(request):
    return render(request, 'vmsAdmin/adminhome.html')


@login_required(login_url='login')
# @admin_only
def adminNotice(request):
    return render(request, 'vmsAdmin/adminnotice.html')


@login_required(login_url='login')
# @admin_only
def adminEditnotice(request):
    return render(request, 'vmsAdmin/admineditnotice.html')


@login_required(login_url='login')
# @admin_only
def adminUserCost(request):
    return render(request, 'vmsAdmin/adminusercost.html')


@login_required(login_url='login')
# @admin_only
def adminUserRequest(request):
    return render(request, 'vmsAdmin/adminuserrequest.html', {
        'requisitions': Requisition.objects.all()
    })


@login_required(login_url='login')
# @admin_only
def adminVehicle(request):
    vehicle = Vehicles.objects.all()
    return render(request, 'vmsAdmin/adminvehicle.html', {'vehicle': vehicle})


@login_required(login_url='login')
def addVehicle(request):
    form = VehicleForm()
    if request.method == 'POST':
        form = VehicleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('AdminVehicle')
    context = {'form': form}
    return render(request, 'vmsAdmin/adminaddvehicle.html', context)


@login_required(login_url='login')
def viewUsers(request):
    User = get_user_model()
    users = User.objects.values()
    return render(request, 'vmsAdmin/viewUser.html', {'user': users})


@login_required(login_url='login')
# @admin_only
def adminDriver(request):
    driver = Drivers.objects.all()
    return render(request, 'vmsAdmin/admindriver.html', {'driver': driver})


@login_required(login_url='login')
def addDriver(request):
    form = DriverForm()
    if request.method == 'POST':
        form = DriverForm(request.POST)
        if form.is_valid():
            driver = form.save(commit=False)
            vehicle = Vehicles.objects.create()
            vehicle.vcl_name = ''
            vehicle.save()
            driver.save()
            return redirect('AdminDriver')
    context = {'form': form}
    return render(request, 'vmsAdmin/adminadddriver.html', context)

# def addDriver(request):
#     form = DriverForm()

#     if request.method == 'POST':
#         form = DriverForm()
#         try:
#             if form.is_valid():
#                 form.save()
#                 return redirect('adminHome')
#         except:
#             print('driver not added')
#     context = {'form': form}
#     return render(request, 'vmsAdmin/add-driver.html', context)
#     # model = Driver
#     # form_class = DriverForm
#     # template_name = 'vmsAdmin/add-driver.html'
#     # success_url = 'admin_home'
