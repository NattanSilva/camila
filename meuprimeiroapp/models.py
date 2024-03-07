from django.db import models

# Create your models here.
class Cadastro(models.Model):
  nome = models.CharField(max_length=20)
  último_nome = models.CharField(max_length=40)
  telefone = models.CharField(max_length=35)
  genero = models.CharField(max_length=10)

  def __str__(self) -> str:
    return f'{self.nome}{self.ultimoo_nome}{self.telefone}{self.genero}'