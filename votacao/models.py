from django.db import models

from django.contrib.auth import get_user_model
User = get_user_model()
# Create your models here.

class eleicao (models.Model):
    nome = models.CharField(('Nome da eleicão:'),  max_length=90)
    descricao  =  models.TextField(("Descricao"))
    inicio = models.DateTimeField(("Data de Inicio da votacao"), auto_now=False, auto_now_add=True)
    fim = models.DateTimeField("Data para a o fim da votacao")
    participantes = models.ManyToManyField(User, verbose_name=("Participantes"))
    total_de_votos = models.IntegerField(("Total de votos"), default=0) 
    foto = models.ImageField(upload_to='Media', blank=False, null=False)
    
    def __str__(self):
        return self.nome 
