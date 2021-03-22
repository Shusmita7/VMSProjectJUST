from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('', views.homePage, name='homePage'),
    path('notice/', views.noticePage, name='noticePage'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout', views.logoutUser, name='logout'),
    path('register/', views.SignUpView.as_view(), name='register'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
