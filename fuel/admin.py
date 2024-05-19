from django.contrib import admin
from .models import Combustivel, Abastecimento, CadCarros, TipoCombustivel

admin.site.register(Combustivel)
admin.site.register(Abastecimento)
admin.site.register(CadCarros)
admin.site.register(TipoCombustivel)