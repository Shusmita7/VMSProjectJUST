from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.accHome, name='AccHome'),
    path('notice/', views.accNotice, name='AccNotice'),
    # path('logbook/', views.LogBookCreate.as_view(), name='logBook'),
    # # path('success/', views.InfoSuccess, name='datainput')
    # re_path('logbook/success/(?P<id>\d+)/$', views.InfoSuccess, name='datainput'),
]
