from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='sub_home'),
    path('notice', views.notice, name='notice'),
    path('schedule', views.schedule, name='schedule'),
    path('view-user', views.viewUser, name='viewUser'),
    path('user-cost', views.userCost, name='userCost'),
    path('requisition-requests', views.requests, name='requests'),
    path('driver', views.driver, name='driver'),
    path('vehicle', views.vehicle, name='vehicle'),
    path('profile', views.profile, name='profile'),
    path('profile/update-profile', views.updateProfile, name='updateProfile'),
]