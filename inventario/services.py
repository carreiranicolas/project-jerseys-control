from django.db import transaction
from django.db.models import DecimalField
from catalogo.models import CamisaTamanho
from inventario.models import Movimentacao


@transaction.atomic #Garante que tudo aconteça ou nada aconteça
def registrar_movimentacao(
    camisa_tamanho: CamisaTamanho,
    tipo: str,
    quantidade: int,
    valor_unitario: DecimalField | None = None,
    observacao: str | None =None
):
    if tipo == 'S':
        if camisa_tamanho.estoque >= quantidade:
            camisa_tamanho.estoque -= quantidade

            camisa_tamanho.save(update_fields=['estoque'])

            valor_unitario = camisa_tamanho.camisa.preco

            return Movimentacao.objects.create(
                camisa_tamanho= camisa_tamanho,
                tipo=tipo,
                quantidade=quantidade,
                valor_unitario = valor_unitario,
                observacao = observacao)
        
        raise ValueError(
            'Não é possível realizar a saída.'
        )
    
    if valor_unitario is None:
        raise ValueError(
            'Para entradas, é necessário inserir o valor do produto.'
        )

    camisa_tamanho.estoque += quantidade

    camisa_tamanho.save(update_fields=['estoque'])

    return Movimentacao.objects.create(
        camisa_tamanho=camisa_tamanho,
        tipo=tipo,
        quantidade=quantidade,
        valor_unitario=valor_unitario,
        observacao=observacao
    )


    


