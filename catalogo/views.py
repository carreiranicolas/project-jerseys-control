from django.shortcuts import render
from .models import Camisa, CamisaTamanho

# Create your views here.


def home(request):

    camisas = Camisa.objects.filter(
        oculto=False
    )

    contexto = {
        'camisas': camisas
    }

    return render(request, 'catalogo/home.html', context=contexto)


def detalhe(request):
    return render(request, 'catalogo/detalhe.html')