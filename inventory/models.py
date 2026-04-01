from django.db import models

# Create your models here.

class Camisa(models.Model):
    time = models.CharField(max_length=100)
    modelo = models.CharField(max_length=50, blank=True)
    tamanho = models.CharField(max_length=10)
    tipo = models.CharField(max_length=20)
    quantidade = models.IntegerField(default=0)
    preco_venda = models.FloatField()

    def __str__(self):
        return f'{self.time} - {self.tamanho}'
