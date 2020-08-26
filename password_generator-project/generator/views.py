from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

def home(request):
    # return HttpResponse("Hello!")
    return render(request, 'generator/home.html', {'password': 'udi2192'})   # render vai direto para PROJECT_NAME/APP_NAME/templates

def password(request):
    characters = []

    if request.GET.get('letraMinuscula'):
        characters.extend(list('abcdefghijklmnopqrstuvwxyz'))
    if request.GET.get('letraMaiuscula'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('numeros'):
        characters.extend(list('0123456789'))
    if request.GET.get('caracteresEspeciais'):
        characters.extend(list('!@#$%&*'))

    length = int(request.GET.get('comprimento', 10))  # default value = 10
    thepassword = ''

    if not len(characters):
        return render(request, 'generator/passworderror.html')
    for eachChar in range(length):
        thepassword += random.choice(characters)

    return render(request, 'generator/password.html', {'password': thepassword})

def about(request):
    return render(request, 'generator/about.html')