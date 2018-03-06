from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Perfil

# Create your views here.
def index(request):
	#retorna lista disponível de perfis no banco
	return render(request, 'index.html',{'perfis': Perfil.objects.all()})

def exibir(request, perfil_id):

	#busca perfil pelo id
	perfil = Perfil.objects.get(id=perfil_id)

	return render(request, 'perfil.html',{'perfil':perfil})

def convidar(request, perfil_id):
	perfil_a_convidar = Perfil.objects.get(id=perfil_id)
	perfil_logado = get_perfil_logado(request)
	perfil_logado.convidar(perfil_a_convidar)
	return redirect('index') # não é necessário repetir o código da primeira função

def get_perfil_logado(request):
	return Perfil.objects.get(id=1)