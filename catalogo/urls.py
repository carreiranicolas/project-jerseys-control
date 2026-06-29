from django.urls import path 
from . import views

app_name = 'catalogo'

urlpatterns = [
    path('', views.home, name='home'),
    path('detalhe', views.detalhe, name='detalhe') #Teste
    # path('detalhe/<int:id>', views.detalhe, name='detalhe')
]
