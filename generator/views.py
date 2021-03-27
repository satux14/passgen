from django.shortcuts import render
from django.http import HttpResponse
import random

def home(request):
    #return HttpResponse('Hello World!!')
    return render(request, 'generator/home.html', {'password':'hsfh()$djh'}) #Password key/value is passed to template

def password(request):
    characters = list('abcdefghijklmnopqrstuvwxyz')
    length = int(request.GET.get('length', 12))
    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*()'))
    if request.GET.get('numbers'):
        characters.extend(list('1234567890'))
    thepassword = ''
    for x in range(length):
        thepassword += random.choice(characters)

    return render(request, 'generator/password.html', {'password':thepassword})

def aboutsite(request):
    return render(request, 'generator/about.html', {'name': 'Password Generator'})
