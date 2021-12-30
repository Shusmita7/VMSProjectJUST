from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.home, name='Home'),
    path('notice/', views.notice, name='Notice'),
    path('requisition/', views.RequisitionCreate.as_view(), name='Requisition'),
    # path('requisition/', views.createRequisition, name='Requisition'),
    re_path('requisition/success/(?P<id>\d+)/$', views.RequisitionSuccess, name='success'),
    path('history/', views.myCost, name='MyCost'),

    # (?P<pk>\d+)/$
]
