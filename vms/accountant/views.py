from django.http import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView, FormView

# from ..accounts.decorators import accountant_only
from .models import LogBook
from .forms import AccForm
from vmsUser.models import Requisition


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
    return HttpResponse("Hello, world. You're at the homepage of accountant.")


@login_required(login_url='login')
# @accountant_only
def notice(request):
    return HttpResponse("This is notice page for accountant")


@login_required(login_url='login')
def logBook(request):
    form = AccForm()
    if request.method == 'POST':
        form = AccForm(request.POST)
        if form.is_valid():
            acc_req = form.save(commit=False)
            requisition = Requisition.objects.create()
            requisition.vcl_type = ''
            requisition.destination = ''
            requisition.save()
            acc_req.save()
            return redirect('acc_home')
    # requisite = Requisition.objects.filter(is_requisited=True).order_by('jour_date')[:1]
    # 'requisite': requisite
    context = {'form': form}
    return render(request, 'accountant/logbook.html', context)


def InfoSuccess(request, id=None):
    return render(request, 'accountant/inputdetails.html', {
        'logbook': get_object_or_404(LogBook, pk=id)
    })


# @method_decorator(login_required(login_url='login'), name='dispatch')
# # @method_decorator(teacher_only, name='dispatch')
# class LogBookCreate(SuccessMessageMixin, CreateView):
#     model = LogBook
#     form_class = AccForm
#     template_name = 'accountant/logbook.html'
#
#     def form_valid(self, form):
#         request = self.request
#         form.save()
#         form.instance.created_by = self.request.user
#         return super().form_valid(form)
