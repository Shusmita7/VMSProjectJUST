from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('notice', views.notice, name='notice'),
    path('schedule', views.schedule, name='schedule'),
    path('view-user', views.viewuser, name='viewuser'),
    path('user-cost', views.usercost, name='usercost'),
    path('requisition-requests', views.requests, name='requests'),
    path('driver', views.driver, name='driver'),
    path('vehicle', views.vehicle, name='vehicle'),
    path('profile', views.profile, name='profile'),
    path('profile/update-profile', views.updateprofile, name='updateprofile'),
]