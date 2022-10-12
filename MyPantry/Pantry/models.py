from unicodedata import category
from django.db import models


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



