from django.shortcuts import render
from django.views.generic import ListView
from portifolio.models import Projeto, Tecnologia


class ListaDeProjetos(ListView):
  model = Projeto
  template_name = 'projeto_list.html'
  context_object_name = 'projetos'

  def get_queryset(self):
    return Projeto.objects.filter(fixado=True)[:3]
  

class ListaDeTodosProjetos(ListView):
  model = Projeto
  template_name = 'projeto_list_all.html'
  context_object_name = 'projetos'