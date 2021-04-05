from django.urls import path
from . import views
urlpatterns = [
    path('', views.subadminHome, name = 'SubadminHome'),
    path('notice/', views.subadminNotice, name = 'SubadminNotice'),
    path('notice/editNotice/', views.subadminEditnotice, name ='subadminEditNotice'),
    path('user-cost/', views.subadminUserCost, name ='SubadminUserCost'),
    path('request/', views.subadminUserRequest, name ='SubaminUserRequest'),
    path('vehicle/', views.subadminVehicle, name ='SubadminVehicle'),
    path('driver/', views.subadminDriver, name ='SubadminDriver'),
]

