from django.urls import path
from user import views

app_name = 'user'


urlpatterns = [
    path('getalluser/', views.get_alluser, name='getalluser'),
    path('adduser/', views.add_user, name='adduser'),
    path('edituser/', views.edit_user, name='edituser'),
    path('getregistinfo/', views.get_registinfo, name='getregistinfo'),
    path('getusermap/', views.get_usermap, name='getusermap'),
]
