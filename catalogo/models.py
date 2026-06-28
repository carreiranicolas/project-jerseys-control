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
            ('S', 'Seleção'),
            ('E', 'Europeia')
        )
    )

    @property
    def nome(self):
        if self.tipo == 'N' or not self.ano_fim:
            return str(self.ano_inicio)
        
        return f'{self.ano_inicio}/{self.ano_fim}'
    
    def __str__(self):
        return self.nome
    

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


    def __str__(self):
        return self.nome




class Camisa(models.Model):
    nome = models.CharField(
        max_length=45,
        null=False,
        blank=False,
    )

    clube = models.ForeignKey(Clube, on_delete=models.PROTECT, related_name="camisas")

    # PROTECT porque: Você não pode excluir o clube enquanto existirem camisas.
    # Se não tivesse, excluiriamos do banco o clube e as camisas ainda apontariam
    #para um clube que não existe
    
    temporada = models.ForeignKey(Temporada, on_delete=models.PROTECT, related_name="camisas")

    tipo = models.CharField(
        max_length=1,
        null=False,
        blank=False,
        default='C',
        choices=(
            ('C', 'Casa'),
            ('F', 'Fora')
        )
    )


    preco = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    descricao = models.TextField()

    oculto = models.BooleanField(default=False)

    criado_em = models.DateTimeField(auto_now_add=True)
    
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.clube} - {self.nome} ({self.temporada})"

        #Exemplo: Barcelona - Home (2026/2027)


class CamisaTamanho(models.Model):
    camisa = models.ForeignKey(Camisa, on_delete=models.CASCADE, related_name="tamanhos")
    estoque = models.PositiveSmallIntegerField(default=0)
    tamanho = models.CharField(
        max_length=3,
        null=False,
        blank=False,
        choices=(
            ('P', 'Pequeno'),
            ('M', 'Médio'),
            ('G', 'Grande'),
            ('GG', 'Extra-Grande')
        )

    )

    oculto = models.BooleanField(default=False)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["camisa", "tamanho"],
                name="unique_camisa_tamanho"
            )
        ]

    def __str__(self):
        return f'{self.tamanho}'

class CamisaMedia(models.Model):
    camisa = models.ForeignKey(Camisa, on_delete=models.CASCADE, related_name="midias")

    tipo_arquivo = models.CharField(
        max_length=1,
        null=False,
        blank=False,
        default='I',
        choices=(
            ('I', 'Imagem'),
            ('V', 'Video')
        )
    )

    ordem = models.PositiveSmallIntegerField(default=1)

    arquivo = models.FileField(upload_to='camisas/')

    class Meta:
        ordering = ["ordem"]

