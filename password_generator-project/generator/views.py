from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

def home(request):
    # return HttpResponse("Hello!")
    return render(request, 'generator/home.html', {'password': 'udi2192'})   # render vai direto para PROJECT_NAME/APP_NAME/templates

def password(request):
    characters = []

    if request.GET.get('lowercase'):
        characters.extend(list('abcdefghijklmnopqrstuvwxyz'))
    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))
    if request.GET.get('specialchars'):
        characters.extend(list('!@#$%&*'))

    length = int(request.GET.get('length', 10))  # default value = 10
    thepassword = ''

    if not len(characters):
        return render(request, 'generator/passworderror.html')
    for eachChar in range(length):
        thepassword += random.choice(characters)

    return render(request, 'generator/password.html', {'password': thepassword})

def about(request):
    return render(request, 'generator/about.html')