from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def movimentacoes(request):
    return render(request, 'inventario/movimentacoes.html')

def nova_movimentacao(request):
    return render(request, 'inventario/nova_movimentacao.html')