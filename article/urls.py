from django.urls import path
from article import views

app_name = 'article'


urlpatterns = [
    path('getallarticle/', views.get_all_article, name='getallarticle'),
    path('editarticle/', views.edit_article, name='editarticle'),
    path('delarticle/', views.del_article, name='delarticle'),
    path('addarticle/', views.add_article, name='addarticle'),
    path('uploadimg/', views.upload_img, name='uploadimg'),
    path('getallimg/', views.get_all_img, name='getallimg'),
]
