from django.shortcuts import render
from django.http import HttpResponse
import json

def cadastro(request):
    
    return HttpResponse('Você está na página de cadastro')
    

def login(request):

    return render(request, 'login.html')


def home(request):

    return HttpResponse('Você está na home do usuário')