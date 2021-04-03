from django.urls import path
from vmsuser import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.home, name = 'Home'),
    path('notice/', views.notice, name = 'Notice'),
    path('requisition/', views.requisitionform, name = 'Requisition'),
    path('history/', views.mycost, name = 'MyCost'),
    # path('', views. , name = ''),
    # path('', views. , name = ''),
    
]

# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.userHome, name='user_home'),
#     path('notice', views.notice, name='notice'),
#     path('requisition', views.requisition, name='requisition'),
#     path('chairman', views.forChairman, name='chairman'),
#     path('user-cost', views.usercost, name='usercost'),
#     path('profile', views.profile, name='profile'),
#     path('profile/update-profile', views.updateprofile, name='updateprofile'),
# ]