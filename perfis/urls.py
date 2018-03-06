"""connectedin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
from . import views
#from perfis import views

urlpatterns = [
    path('',views.index, name='index'),
    #re_path(r'^perfis/(?P<perfil_id>\d+)$', views.exibir, name='exibir')
    #para não repetir 'perfis/<int:perfil_id>/', definimos como prefixo
    path('perfis/<int:perfil_id>/', include([
    	path('',views.exibir, name='exibir'),
    	path('convidar/', views.convidar, name='convidar'),
    	])),
]
