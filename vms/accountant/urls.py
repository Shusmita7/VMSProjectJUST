from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='acc_home'),
    path('notice', views.notice, name='notice'),
    path('logbook', views.logBook, name='logBook'),
]
