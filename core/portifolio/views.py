from django.shortcuts import render
from django.views.generic import ListView
from portifolio.models import Projeto, Tecnologia

# Create your views here.

class ListaDeProjetos(ListView):
  model = Projeto
  template_name = 'projeto_list.html'
  context_object_name = 'projetos'