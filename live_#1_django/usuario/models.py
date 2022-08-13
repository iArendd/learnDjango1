from django.db import models



class Usuario(models.Model):

    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100)
    idade = models.IntegerField()
    ativo = models.BooleanField(default=False)