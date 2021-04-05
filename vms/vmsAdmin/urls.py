from django.urls import path
from . import views

urlpatterns = [
    path('', views.adminHome, name='AdminHome'),
    path('notice/', views.adminNotice, name='AdminNotice'),
    path('notice/edit-notice/', views.adminEditnotice, name='adminEditNotice'),
    path('user-cost/', views.adminUserCost, name='AdminUserCost'),
    path('request/', views.adminUserRequest, name='AdminUserRequest'),
    path('vehicle/', views.adminVehicle, name='AdminVehicle'),
    path('vehicle/add-vehicle/', views.adminAddvehicle, name='adminAddVehicle'),
    path('driver/', views.adminDriver, name='AdminDriver'),
    path('driver/add-driver/', views.adminAdddriver, name='adminAddDriver'),
]
