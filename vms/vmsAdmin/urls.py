from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('notice', views.notice, name='notice'),
    path('schedule', views.schedule, name='schedule'),
    path('view-user', views.vmsUser, name='viewUser'),
    path('add-user', views.vmsUser, name='addUser'),
    path('manage-user', views.vmsUser, name='manageUser'),
    path('user-cost', views.userCost, name='userCost'),
    path('requisition-requests', views.requests, name='requests'),
    path('driver', views.driver, name='driver'),
    path('vehicle', views.vehicle, name='vehicle'),
    path('profile', views.profile, name='profile'),
    path('profile/update-profile', views.updateProfile, name='updateProfile'),
]