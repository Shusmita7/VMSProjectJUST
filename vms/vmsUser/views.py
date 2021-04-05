from django.shortcuts import render, redirect
from django.views.generic import CreateView, FormView

from .forms import RequisitionForm
from .models import Requisition


def home(request):
    return render(request, 'vmsUser/userhome.html')


def notice(request):
    return render(request, 'vmsUser/usernotice.html')


class RequisitionformsView(FormView):
    model = Requisition
    form_class = RequisitionForm
    template_name = 'vmsUser/userrequisition.html'
    success_url = 'Home'

    def requisition(self, form):
        form = RequisitionForm()
        try:
            if form.is_valid():
                form.save()
                return redirect('Home')
        except:
                print('Requisition not added')
        context = {'form': form}
        return render('vmsUser/userrequisition.html', context)


# def requisitionform(request):
#     return render(request, 'vmsUser/userrequisition.html')


def mycost(request):
    return render(request, 'vmsUser/usermyCost.html')
