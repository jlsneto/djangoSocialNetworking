from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Perfil
from .models import Convite

# Create your views here.
def index(request):
	#retorna lista disponível de perfis no banco
	return render(request, 'index.html',{'perfis': Perfil.objects.all(), 'perfil_logado':get_perfil_logado(request) })

def exibir(request, perfil_id):
	#busca perfil pelo id
	perfil = Perfil.objects.get(id=perfil_id)
	perfil_logado = get_perfil_logado(request)
	ja_eh_contato = perfil in perfil_logado.contatos.all()

	convidados = [convite.convidado for convite in perfil_logado.solicitacoes_enviadas.all()]
	enviou_convite = perfil in convidados

	return render(request, 'perfil.html',{'perfil':perfil, 'perfil_logado':get_perfil_logado(request), 'ja_eh_contato':ja_eh_contato, 'enviou_convite':enviou_convite})

def convidar(request, perfil_id):
	perfil_a_convidar = Perfil.objects.get(id=perfil_id)
	perfil_logado = get_perfil_logado(request)
	perfil_logado.convidar(perfil_a_convidar)
	return redirect('index') # não é necessário repetir o código da primeira função

def aceitar(request, convite_id):
	convite = Convite.objects.get(id=convite_id)
	convite.aceitar()
	return redirect('index')

def get_perfil_logado(request):
	return Perfil.objects.get(id=1)