from django.shortcuts import render
from .models import *


# Create your views here.

def cadastro (request):
    if request.method == 'POST':
        data_usuario = Login()
        data_usuario.username = request.POST['username']
        data_usuario.senha = request.POST['senha']
        data_usuario.save()

        args = {
            'logado': 'Você conseguiu logar!, agora vai se divertir com o jogos da Academia7'
        }
    return render(request, 'index.html')

def login(request):
    if request.method == "POST":
        formulario_username = request.POST['username']
        formulario_senha = request.POST['senha']

        username_logado = Login.objects.filter(username__username = formulario_username).first()
                                            #    username__senha = formulario_senha).first()
                        
        
        if username_logado is not None:
            args = {
                'dados': username_logado
            }
            return render(request, 'teste.html', args)
        else:
            args = {
                'msg': 'Noooooosssa, credenciais inválidas'
            }
            return render(request, 'login.html', args)

    return render(request, 'login.html')

def velha(request):
    return render(request, 'velha.html')