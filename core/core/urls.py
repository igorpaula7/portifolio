from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from portifolio.views import ListaDeProjetos

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ListaDeProjetos.as_view(), name='lista_projetos')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
