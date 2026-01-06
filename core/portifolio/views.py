from django.views.generic import ListView
from portifolio.models import Projeto


class ListaProjetos(ListView):
    model = Projeto
    context_object_name = 'projetos'
    mostrar_todos = False

    def get_template_names(self):
        if self.mostrar_todos:
            return ['projeto_list_all.html']
        return ['projeto_list.html']

    def get_queryset(self):
        qs = super().get_queryset()
        if self.mostrar_todos:
            return qs
        return qs.filter(fixado=True)[:3]
