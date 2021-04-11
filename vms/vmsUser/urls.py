from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='Home'),
    path('notice/', views.notice, name='Notice'),
    path('requisition/', views.createRequisition, name='Requisition'),
    # path('requisition/success', views.RequisitionSuccess, name='Requisition-success'),
    # path('requisition-details', views.RequisitionDetail, name='requisition-detail'),
    path('history/', views.myCost, name='MyCost'),

]
