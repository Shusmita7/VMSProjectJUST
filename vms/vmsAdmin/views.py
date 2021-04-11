from django.shortcuts import render
from django.shortcuts import redirect
from django.views.generic import CreateView, FormView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from .forms import DriverForm, VehicleForm
from .models import Drivers, Vehicles


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
    return render(request, 'vmsAdmin/adminuserrequest.html')


@login_required(login_url='login')
# @admin_only
def adminVehicle(request):
    vehicle = Vehicles.objects.all()
    return render(request, 'vmsAdmin/adminvehicle.html', {'vehicle': vehicle})


# @method_decorator(login_required(login_url='login'), name='dispatch')
# # @method_decorator(admin_only, name='dispatch')
# class addVehiclesView(FormView):
#     model = Vehicles
#     form_class = VehicleForm
#     template_name = 'vmsAdmin/adminaddvehicle.html'
#     success_url = 'AdminHome'
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


# @login_required(login_url='login')
# @admin_only
# def adminAddvehicle(request):
#     return render(request, 'vmsAdmin/adminaddvehicle.html')


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
# @method_decorator(login_required(login_url='login'), name='dispatch')
# # @method_decorator(admin_only, name='dispatch')
# class addDriverView(FormView):
#     model = Drivers
#     form_class = DriverForm
#     template_name = 'vmsAdmin/adminadddriver.html'
#     success_url = 'AdminHome'
#
#
# @login_required(login_url='login')
# # @admin_only
# def adminAdddriver(request):
#     return render(request, 'vmsAdmin/adminadddriver.html')

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
