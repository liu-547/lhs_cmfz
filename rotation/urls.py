from django.urls import path
from rotation import views

app_name = 'rotation'


urlpatterns = [
    path('getall/', views.get_all, name='getall'),
    path('add/', views.add, name='add'),
    path('edit/', views.edit, name='edit'),
]
