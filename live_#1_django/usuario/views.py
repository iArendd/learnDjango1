from django.shortcuts import render
from django.http import HttpResponse
import json

def cadastro(request):
    
    return HttpResponse('Você está na página de cadastro')
    

def login(request):

    nome = request.GET.get('nome')
    sobrenome = request.GET.get('sobrenome')
    return render(request, 'login/login.html', {'nome_usuario': nome, 'sobrenome_usuario': sobrenome})

def home(request):

    return HttpResponse('Você está na home do usuário')