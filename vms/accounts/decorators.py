# from django.shortcuts import redirect
#
#
# def unauthenticated_user(view_func):
#     def wrapper_func(request, *args, **kwargs):
#         if request.user.is_authenticated:
#             return redirect('AdminHome')
#         else:
#             return view_func(request, *args, **kwargs)
#
#     return wrapper_func


# def allowed_users(allowed_roles=[]):
#     def decorator(view_func):
#         def wrapper_func(request, *args, **kwargs):
#             group = None
#             if request.user.groups.exists():
#                 group = request.user.groups.all()[0].name
#             if group in allowed_roles:
#                 return view_func(request, *args, **kwargs)
#             else:
#                 HttpResponse('You are not authorized to view this page')
#
#         return wrapper_func
#
#     return decorator


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


# def chairman_only(view_func):
#     def wrapper_func(request, *args, **kwargs):
#         group = None
#         if request.user.groups.exists():
#             group = request.user.groups.all()[0].name
#         if group == 'admin':
#             return redirect('AdminHome')
#         if group == 'teacher':
#             return redirect('Home')
#         if group == 'subadmin':
#             return redirect('SubadminHome')
#         if group == 'accountant':
#             return redirect('acc_home')
#         if group == 'chairman':
#             return view_func(request, *args, **kwargs)
#
#     return wrapper_func


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


# def teacher_only(view_func):
#     def wrapper_func(request, *args, **kwargs):
#         group = None
#         if request.user.groups.exists():
#             group = request.user.groups.all()[0].name
#         if group == 'chairman':
#             return redirect('Home')
#         if group == 'admin':
#             return redirect('AdminHome')
#         if group == 'subadmin':
#             return redirect('SubadminHome')
#         if group == 'accountant':
#             return redirect('acc_home')
#         if group == 'teacher':
#             return view_func(request, *args, **kwargs)
#
#     return wrapper_func


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
