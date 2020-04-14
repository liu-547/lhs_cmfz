from django.urls import path
from rbac import views

app_name = 'rbac'


urlpatterns = [
    path('loginform/', views.login, name='loginform'),
    path('loginlogic/', views.login_logic, name='loginlogic'),
]
