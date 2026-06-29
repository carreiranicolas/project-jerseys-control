from django.contrib import admin
from .models import Temporada, Clube, Camisa, CamisaTamanho, CamisaMedia



admin.site.register(Temporada)
admin.site.register(Clube)
admin.site.register(Camisa)
admin.site.register(CamisaTamanho)
admin.site.register(CamisaMedia)

# Register your models here.
