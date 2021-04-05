from django.urls import path

from . import views

urlpatterns = [
    path('', views.homePage, name='homePage'),
    path('notice/', views.noticePage, name='noticePage'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout', views.logoutUser, name='logout'),
    path('register/', views.SignUpView.as_view(), name='register'),
]


