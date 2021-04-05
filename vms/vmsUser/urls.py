from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='Home'),
    path('notice/', views.notice, name='Notice'),
    path('requisition/', views.RequisitionformsView.as_view(), name='Requisition'),
    path('history/', views.mycost, name='MyCost'),

]
