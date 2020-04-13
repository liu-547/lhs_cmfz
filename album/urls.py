from django.urls import path
from album import views

app_name = 'album'


urlpatterns = [
    path('getallalbum/', views.get_all_album, name='getallalbum'),
    path('getallchapter/', views.get_all_chapter, name='getallchapter'),
    path('editalbum/', views.edit_album, name='editalbum'),
    path('editchapter/', views.edit_chapter, name='editchapter'),
    path('addalbum/', views.add_album, name='addalbum'),
    path('addchapter/', views.add_chapter, name='addchapter'),
]
