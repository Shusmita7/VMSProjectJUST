from django.shortcuts import render
from django.http import HttpResponse, request
from django.shortcuts import redirect
from django.views.generic import CreateView, FormView

from .forms import DriverForm, VehicleForm
from .models import Driver, Vehicle


def adminHome(request):
    return HttpResponse("Hello, world. You're at the homepage of user.")


def notice(request):
    return HttpResponse("This is notice page")


def schedule(request):
    return HttpResponse("This is schedule page")


def vmsUser(request):
    return HttpResponse("This is User Page")


def userCost(request):
    return HttpResponse("This is user cost page")


def requests(request):
    return HttpResponse("This is requisition request page")


def driver(request):
    return HttpResponse("This is vehicle page")


def addDriver(request):
    form = DriverForm()

    if request.method == 'POST':
        form = DriverForm()
        try:
            if form.is_valid():
                form.save()
                return redirect('adminHome')
        except:
            print('driver not added')
    context = {'form': form}
    return render(request, 'vmsAdmin/add-driver.html', context)
    # model = Driver
    # form_class = DriverForm
    # template_name = 'vmsAdmin/add-driver.html'
    # success_url = 'admin_home'


class addVehiclesView(FormView):
    model = Vehicle
    form_class = VehicleForm
    template_name = 'vmsAdmin/add-vehicle.html'
    success_url = 'admin_home'


def vehicle(request):
    return HttpResponse("This is vehicle page")


def profile(request):
    return HttpResponse("This is profile page")


def updateProfile(request):
    return HttpResponse("This is Update profile page")
