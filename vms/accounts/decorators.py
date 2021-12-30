from django.shortcuts import redirect


# def unauthenticated_user(view_func):
#     def wrapper_func(request, *args, **kwargs):
#         if request.user.is_authenticated:
#             return redirect('AdminHome')
#         else:
#             return view_func(request, *args, **kwargs)
#
#     return wrapper_func
#
#
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


def gadmin_only(view_func):
    def wrapper_func(request, *args, **kwargs):
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name
        if group == 'gchairman':
            return redirect('Home')
        if group == 'guser':
            return redirect('Home')
        if group == 'gsubadmin':
            return redirect('SubadminHome')
<<<<<<< Updated upstream
        if group == 'agccountant':
=======
        if group == 'gaccountant':
>>>>>>> Stashed changes
            return redirect('acc_home')
        if group == 'gadmin':
            return view_func(request, *args, **kwargs)
        else:
            return redirect('AdminHome')

    return wrapper_func


def gchairman_only(view_func):
    def wrapper_func(request, *args, **kwargs):
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name
        if group == 'gadmin':
            return redirect('AdminHome')
        if group == 'guser':
            return redirect('Home')
        if group == 'gsubadmin':
            return redirect('SubadminHome')
        if group == 'gaccountant':
            return redirect('acc_home')
        if group == 'gchairman':
            return view_func(request, *args, **kwargs)
        else:
            return redirect('Home')

    return wrapper_func


def gsubadmin_only(view_func):
    def wrapper_func(request, *args, **kwargs):
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name
        if group == 'gchairman':
            return redirect('Home')
        if group == 'guser':
            return redirect('Home')
        if group == 'gadmin':
            return redirect('AdminHome')
        if group == 'gaccountant':
            return redirect('acc_home')
        if group == 'gsubadmin':
            return view_func(request, *args, **kwargs)
        else:
            return redirect('SubadminHome')

    return wrapper_func


def guser_only(view_func):
    def wrapper_func(request, *args, **kwargs):
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name
        if group == 'gchairman':
            return redirect('Home')
        if group == 'gadmin':
            return redirect('AdminHome')
        if group == 'gsubadmin':
            return redirect('SubadminHome')
        if group == 'gaccountant':
            return redirect('acc_home')
        if group == 'guser':
            return view_func(request, *args, **kwargs)
        else:
            return redirect('Home')

    return wrapper_func


def gaccountant_only(view_func):
    def wrapper_func(request, *args, **kwargs):
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name
        if group == 'gchairman':
            return redirect('Home')
        if group == 'guser':
            return redirect('Home')
        if group == 'gsubadmin':
            return redirect('SubadminHome')
        if group == 'gadmin':
            return redirect('AdminHome')
        if group == 'gaccountant':
            return view_func(request, *args, **kwargs)
        else:
            return redirect('acc_home')

    return wrapper_func
