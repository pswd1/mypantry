from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'Pantry/home.html')

def search(request):
    return render(request, 'Pantry/search.html')
