from django.urls import path
from . import views

app_name = 'inventario'


urlpatterns = [
    path('', views.movimentacoes, name='movimentacoes'),
    path('nova_movimentacao/', views.nova_movimentacao, name='nova_movimentacao')
]
