from django.db import models

# Create your models here. 


class Temporada(models.Model):
    ano_inicio = models.PositiveSmallIntegerField()
    ano_fim = models.PositiveSmallIntegerField(null=True, blank=True)

    tipo = models.CharField(
        max_length=1,
        default='N',
        null=False,
        blank=False,
        choices=(
            ('N', 'Nacional'),
            ('S', 'Seleção')
            ('E', 'Europeia')
        )
    )

    @property
    def nome(self):
        if self.tipo == 'N':
            return str(self.ano_inicio)
        
        return f'{self.ano_inicio}/{self.ano_fim}'
    

class Clube(models.Model):
    nome = models.CharField(
        max_length=45,
        null=False,
        blank=False,
        unique=True
    )

    oculto = models.BooleanField(default=False)

    criado_em = models.DateTimeField(auto_now_add=True)

    atualizado_em = models.DateTimeField(auto_now=True)

    excluido_em = ...




class Camisa(models.Model):
    nome = models.CharField(
        max_length=45,
        null=False,
        blank=False,
        unique=True
    )

    clube = ... #Foreign Key com clube
    
    temporada = ... #Foreign Key com temporada


    preco = models.FloatField()

    descricao = models.TextField()

    oculto = models.BooleanField(default=False)

    criado_em = models.DateTimeField(auto_now_add=True)
    
    atualizado_em = models.DateTimeField(auto_now=True)

    excluido_em = ...


class CamisaTamanho(models.Model):
    camisa = ... #Foreign Key com camisa


class CamisaMedia(models.Model):
    camisa = ... # Foreign Key com camisa


