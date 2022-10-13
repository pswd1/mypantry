from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from . forms import UserForm, recipeForm, ingredientForm
from Pantry.models import ingredient, recipe
from django import forms

def home(request):
    return render(request, 'Pantry/dashboard.html')

def userlogin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return render(request, 'Pantry/dashboard.html')
        else:
            return render(request, 'Pantry/login.html', {'error_message':'Login credentials are wrong'})
    return render(request, 'Pantry/login.html')

def userlogout(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, 'Pantry/login.html', context)

def register(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return render(request, 'Pantry/login.html')
    context = {
        "form": form,
    }
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
