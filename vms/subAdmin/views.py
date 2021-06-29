from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from accounts.decorators import gsubadmin_only


@login_required(login_url='login')
@gsubadmin_only
def subadminHome(request):
    return render(request, 'subAdmin/subadminhome.html')


@login_required(login_url='login')
@gsubadmin_only
def subadminNotice(request):
    return render(request, 'subAdmin/subadminnotice.html')


@login_required(login_url='login')
@gsubadmin_only
def subadminEditnotice(request):
    return render(request, 'subAdmin/subadmineditnotice.html')


@login_required(login_url='login')
@gsubadmin_only
def subadminUserCost(request):
    return render(request, 'subAdmin/subadminusercost.html')


@login_required(login_url='login')
@gsubadmin_only
def subadminUserRequest(request):
    return render(request, 'subAdmin/subadminuserrequest.html')


@login_required(login_url='login')
@gsubadmin_only
def subadminVehicle(request):
    return render(request, 'subAdmin/subadminvehicle.html')


@login_required(login_url='login')
@gsubadmin_only
def subadminDriver(request):
    return render(request, 'subAdmin/subadmindriver.html')

