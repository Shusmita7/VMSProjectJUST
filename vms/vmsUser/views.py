from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView, FormView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.contrib.auth import get_user_model

from .forms import RequisitionForm
from .models import Requisition
User = get_user_model()

# from ..accounts.decorators import teacher_only


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


@login_required(login_url='login')
# @teacher_only
def home(request):
    return render(request, 'vmsUser/userhome.html')


@login_required(login_url='login')
# @teacher_only
def notice(request):
    return render(request, 'vmsUser/usernotice.html')


#
# @method_decorator(login_required(login_url='login'), name='dispatch')
# # @method_decorator(teacher_only, name='dispatch')
# class RequisitionCreate(SuccessMessageMixin, CreateView):
#     model = Requisition
#     form_class = RequisitionForm
#     template_name = 'vmsUser/userrequisition.html'
#
#     # success_url = '/success/'
#     # success_message = "Requisition Successful"
#
#     def form_valid(self, form):
#         # request = self.request
#         # form.save()
#         # form.instance.created_by = self.request.user
#         # # messages.success('You have successfully completed your requisition request')
#         # return super().form_valid(form)
#         response = super().form_valid(form)
#         success_message = self.get_success_message("Requisition Successful")
#         if success_message:
#             messages.success(self.request, success_message)
#             # redirect('Home')
#         return response


# def requisitionform(request):
#     return render(request, 'vmsUser/userrequisition.html')
@login_required(login_url='login')
def createRequisition(request):
    form = RequisitionForm()
    if request.method == 'POST':
        form = RequisitionForm(request.POST)
        if form.is_valid():
            requisition = form.save(commit=False)
            userreq = User.objects.create()
            userreq.username = request.user
            userreq.email = ''
            userreq.full_name = ''
            userreq.designation = ''
            userreq.dept_sec = ''
            userreq.contact_no = ''
            userreq.save()
            requisition.save()

            return redirect('Home')
    context = {'form': form}
    return render(request, 'vmsUser/userrequisition.html', context)


# def RequisitionSuccess(request):
#     messages.success('You have successfully completed your requisition request')
#     return request
#
#
# def RequisitionDetail(request, pk):
#     return render(request, 'requisitionDetail.html', {
#         'requisition': get_object_or_404(Requisition, pk=id)
#     })


@login_required(login_url='login')
# @teacher_only
def myCost(request):
    return render(request, 'vmsUser/usermyCost.html', {
        'requisitions': Requisition.objects.all()
    })
