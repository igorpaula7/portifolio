from django.db import models


class Tecnologia(models.Model):
    nome = models.CharField(max_length=30)

    def __str__(self):
        return self.nome


class Projeto(models.Model):
    titulo = models.CharField(max_length=30)
    descricao = models.TextField()
    link_repositorio = models.URLField()
    tecnologias = models.ManyToManyField(Tecnologia)
    imagem_capa = models.ImageField(
        upload_to="projetos/",  # pasta dentro de media/
        blank=True,
        null=True,
    )
    fixado = models.BooleanField(default=False)

    def __str__(self):
        return self.titulo

    class Meta:
        ordering = ["-fixado", "-id"]
