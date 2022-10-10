from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

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

def createRecipe(request):
    return render(request, 'Pantry/create_recipe.html')

def updateRecipe(request):
    return render(request, 'Pantry/update_recipe.html')

def deleteRecipe(request):
    return render(request, 'Pantry/delete_recipe.html')
