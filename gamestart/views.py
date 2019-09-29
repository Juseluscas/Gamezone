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

def login(request):
    if request.method == "POST":
        formulario_username = request.POST['username']
        formulario_senha = request.POST['senha']
        
    return render(request, 'login.html')
        # usuario_logado = Login.objects.filter(usuario__username = formulario_username,
        #                                       usuario__senha = formulario_senha).first()

        # if usuario_logado is not None:
        #         args = {
        #             'dados': usuario_logado
        #         }
        #         return render(request, 'teste.html', args)
        # else:
        #         args = {
        #             'msg': 'Noooooosssa, credenciais inválidas'
        #         }
        #         return render(request, 'login.html', args)