from django.urls import path
from . import views

#You will need to change some of these urls to be dynamic.
#https://docs.djangoproject.com/en/4.0/topics/http/urls/

urlpatterns = [
    path('', views.home, name='home'),
    path('userlogin/', views.userlogin, name='userlogin'),
    path('userlogout/', views.userlogout, name='userlogout'),
    path('register', views.register, name='register'),
    path('pantry/', views.pantry, name='pantry'),
    path('browse/', views.browse, name='browse'),
    path('viewRecipe/', views.viewRecipe, name='view'),
    path('myRecipes/', views.myRecipes, name='saved'),
    path('createRecipe/', views.createRecipe, name='create'),
    path('updateRecipe/', views.updateRecipe, name='update'),
    path('deleteRecipe/', views.deleteRecipe, name='delete'),
]