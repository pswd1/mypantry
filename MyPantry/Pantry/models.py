from dataclasses import fields
from unicodedata import category
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class ingredient(models.Model):
    name =  models.CharField(max_length=255)
    quantity = models.CharField(max_length=20)
    unit =  models.CharField(max_length=50)
    
class recipe(models.Model):
    title = models.CharField(max_length=255)
    #directions = models.SlugField(unique=True, max_length=255)
    directions = models.TextField
    content = models.TextField()
    ingredients = models.ForeignKey(ingredient,on_delete=models.CASCADE)
    category = models.CharField(max_length=255)

class UserModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

