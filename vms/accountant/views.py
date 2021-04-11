from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# from ..accounts.decorators import accountant_only


# def accountant_only(view_func):
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
#         if group == 'admin':
#             return redirect('AdminHome')
#         if group == 'accountant':
#             return view_func(request, *args, **kwargs)
#
#     return wrapper_func



@login_required(login_url='login')
# @accountant_only
def home(request):
    return HttpResponse("Hello, world. You're at the homepage of user.")


@login_required(login_url='login')
# @accountant_only
def notice(request):
    return HttpResponse("This is notice page")


@login_required(login_url='login')
# @accountant_only
def logBook(request):
    return HttpResponse("This is log book page for accountant.")
