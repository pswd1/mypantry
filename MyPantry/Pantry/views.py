from django.shortcuts import render, redirect
from django.http import HttpResponse
from django import forms
from Pantry.forms import recipeForm, ingredientForm
from Pantry.models import ingredient, recipe

def home(request):
    return render(request, 'Pantry/dashboard.html')

def login(request):
    return render(request, 'Pantry/login.html')

def register(request):
    return render(request, 'Pantry/register.html')

def pantry(request):
    return render(request, 'Pantry/pantry.html')

def browse(request):
    return render(request, 'Pantry/browse.html')

def viewRecipe(request):
    return render(request, 'Pantry/view_recipe.html')

def myRecipes(request):
    return render(request, 'Pantry/saved_recipes.html')

#@login_Reqired
def createRecipe(request):
    #TODO: add the ingredients to the form (see forms.py)

    context={}
    form = recipeForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
    context['form']= form
    return render(request, 'Pantry/create_recipe.html', context)

def updateRecipe(request):
    return render(request, 'Pantry/update_recipe.html')

def deleteRecipe(request):
    return render(request, 'Pantry/delete_recipe.html')
