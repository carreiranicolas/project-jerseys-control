from django.db import models

# Create your models here.

# Ainda falta bastante coisa

class Movimentacao(models.Model):

    camisa = ... #Será a Foreign Key com CamisaTamanho

    tipo = models.CharField(
        default='E',
        max_length=1,
        choices=(
            
            ('E', 'Entrada'),
            ('S', 'Saída')
        ),
        null=False,
        blank=False
    )

    observacao = models.TextField()

    criada_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Movimentação: {self.pk} - {self.criada_em}'