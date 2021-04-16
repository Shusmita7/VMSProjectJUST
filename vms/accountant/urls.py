from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.home, name='acc_home'),
    path('notice/', views.notice, name='notice'),
    path('logbook/', views.logBook, name='logBook'),
    # path('success/', views.InfoSuccess, name='datainput')
    re_path('logbook/success/(?P<id>\d+)/$', views.InfoSuccess, name='datainput'),
]
