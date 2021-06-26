from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# from ..accounts.decorators import subadmin_only


# def subadmin_only(view_func):
#     def wrapper_func(request, *args, **kwargs):
#         group = None
#         if request.user.groups.exists():
#             group = request.user.groups.all()[0].name
#         if group == 'chairman':
#             return redirect('Home')
#         if group == 'teacher':
#             return redirect('Home')
#         if group == 'admin':
#             return redirect('AdminHome')
#         if group == 'accountant':
#             return redirect('acc_home')
#         if group == 'subadmin':
#             return view_func(request, *args, **kwargs)
#
#     return wrapper_func


@login_required(login_url='login')
# @subadmin_only
def subadminHome(request):
    return render(request, 'subAdmin/subadminhome.html')


@login_required(login_url='login')
# @subadmin_only
def subadminNotice(request):
    return render(request, 'subAdmin/subadminnotice.html')


@login_required(login_url='login')
# @subadmin_only
def subadminEditnotice(request):
    return render(request, 'subAdmin/subadmineditnotice.html')


@login_required(login_url='login')
# @subadmin_only
def subadminUserCost(request):
    return render(request, 'subAdmin/subadminusercost.html')


@login_required(login_url='login')
# @subadmin_only
def subadminUserRequest(request):
    return render(request, 'subAdmin/subadminuserrequest.html')


@login_required(login_url='login')
# @subadmin_only
def subadminVehicle(request):
    return render(request, 'subAdmin/subadminvehicle.html')


@login_required(login_url='login')
# @subadmin_only
def subadminDriver(request):
    return render(request, 'subAdmin/subadmindriver.html')

