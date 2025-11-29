from django.db import models

class Tecnologia(models.Model):
  nome = models.CharField(max_length=30)
  cor_fundo = models.CharField(max_length=7)
  cor_texto = models.CharField(max_length=7)

  def __str__(self):
    return self.nome 
  
class Projeto(models.Model):
  titulo = models.CharField(max_length=30)
  descricao = models.TextField()
  link_repositorio = models.URLField()
  tecnologias = models.ManyToManyField(Tecnologia)
  imagem_capa = models.ImageField(
    upload_to='projetos/',  # pasta dentro de media/
    blank=True,
    null=True
  )

  def __str__(self):
    return self.titulo