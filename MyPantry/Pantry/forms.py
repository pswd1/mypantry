from django import forms
from django.forms import ModelForm
from .models import ingredient, recipe

class ingredientForm(ModelForm):
    class Meta:
        model = ingredient
        fields ="__all__"

class recipeForm(ModelForm):
    class Meta:
        model = recipe
        #ingredients was not working with the forms more investigation is needed
        exclude = ['ingredients']
        #fields = "__all__"