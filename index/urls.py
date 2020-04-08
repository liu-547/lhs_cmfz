from django.urls import path
from index import views

app_name = 'index'


urlpatterns = [
    path('index/', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('getcode/', views.get_code, name='getcode'),
    path('checkuser/', views.check_user, name='checkuser'),
]
