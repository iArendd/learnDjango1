from django.shortcuts import render
from django.http import HttpResponse
import json
from .models import Usuario

def cadastro(request):
    
    return HttpResponse('Você está na página de cadastro')
    

def login(request):

    nome = request.GET.get('nome')
    sobrenome = request.GET.get('sobrenome')
    return render(request, 'login/login.html', {'nome_usuario': nome, 'sobrenome_usuario': sobrenome})


def home(request):

    return HttpResponse('Você está na home do usuário')


def salvar(request):

    nome = request.POST.get('nome')
    sobrenome = request.POST.get('sobrenome')
    idade = request.POST.get('idade')

    usuario = Usuario(

        nome = nome,
        sobrenome = sobrenome,
        idade = idade

    )

    usuario.save()

    return HttpResponse(f"{nome} {sobrenome} {idade}")