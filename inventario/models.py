from django.db import models
from catalogo.models import CamisaTamanho

# Create your models here.


# Algo importante sobre os models é que:

# O Model não deveria saber:

# enviar email
# alterar outro model
# gerar dashboard
# registrar logs

# Ele só precisa responder perguntas sobre ele. Usar ele mesmo.

# Se eu preciso de uma regra de negócio de registrar movimentação, por exemplo:

# def registrar_movimentacao(...):

#     validar estoque

#     atualizar estoque

#     criar movimentação

#     salvar

# Model: "O que eu sou?" (estrutura dos dados e comportamentos que dependem apenas da própria entidade).
# View: "Quem chamou e qual resposta devo devolver?" (HTTP, formulários, redirecionamentos, templates, JSON).
# Service: "O que precisa acontecer para cumprir este caso de uso?" (regras de negócio envolvendo uma ou mais entidades).


class Movimentacao(models.Model):

    camisa_tamanho = models.ForeignKey(CamisaTamanho, on_delete=models.PROTECT, related_name='movimentacoes') #Será a Foreign Key com CamisaTamanho

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

    quantidade = models.PositiveSmallIntegerField(default=1)

    valor_unitario = models.DecimalField(
        max_digits=10,
        decimal_places=2
    ) 
    
    # O valor não foi calculado na view porque se puxar da camisa, perderemos o histórico
    # de quanto valia uma camisa. Exemplo: data x foi vendida por 180 e data y foi por 200.
    # Perderemos esse histórico porque os valores passarão a ser buscado de CamisaTamanho

    observacao = models.TextField(null=True, blank=True)

    data_movimentacao = models.DateTimeField()

    criada_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (
            f"{self.get_tipo_display()} - "
            f"{self.camisa_tamanho.camisa.nome} "
            f"({self.camisa_tamanho.tamanho})"
        )
    
    @property
    def valor_total(self):
        return self.quantidade * self.valor_unitario
    
    