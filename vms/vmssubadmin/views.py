from django.shortcuts import render
from django.shortcuts import redirect
# from django.views.generic import CreateView, FormView


# from .forms import DriverForm, VehicleForm
# from .models import Drivers, Vehicles

def subadminHome(request):
    return render(request, 'vmssubadmin/subadminhome.html')

def subadminNotice(request):
    return render(request, 'vmssubadmin/subadminnotice.html')

def subadminEditnotice(request):
    return render(request, 'vmssubadmin/subadmineditnotice.html')

def subadminUserCost(request):
    return render(request, 'vmssubadmin/subadminusercost.html')

def subadminUserRequest(request):
    return render(request, 'vmssubadmin/subadminuserrequest.html')

def subadminVehicle(request):
    return render(request, 'vmssubadmin/subadminvehicle.html')

def subadminDriver(request):
    return render(request, 'vmssubadmin/subadmindriver.html')

# from django.shortcuts import render
# from django.http import HttpResponse


# def home(request):
#     return HttpResponse("Hello, world. You're at the homepage of sub-admin.")


# def notice(request):
#     return HttpResponse("This is notice page")


# def schedule(request):
#     return HttpResponse("This is schedule page")


# def viewUser(request):
#     return HttpResponse("This is View User list page")


# def userCost(request):
#     return HttpResponse("This is user cost page")


# def requests(request):
#     return HttpResponse("This is requisition request page")


# def driver(request):
#     return HttpResponse("This is vehicle page")


# def vehicle(request):
#     return HttpResponse("This is vehicle page")


# def profile(request):
#     return HttpResponse("This is profile page")


# def updateProfile(request):
#     return HttpResponse("This is Update profile page")
