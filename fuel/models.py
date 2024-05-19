from django.db import models
from django.contrib.auth.models import User

class Combustivel(models.Model):
    nome = models.CharField(max_length=30)

    def __str__(self):
        return self.nome


class Abastecimento(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, default=1)
    veiculo = models.CharField(max_length=50, default='')
    data_abastecimento = models.DateField()
    combustivel = models.CharField(max_length=10)
    posto = models.CharField(max_length=30, default='')
    km_inicial = models.IntegerField()
    km_final = models.IntegerField()
    litros_abastecidos = models.FloatField()
    custo_total = models.FloatField()

    def __str__(self):
        return self.veiculo

class TipoCombustivel(models.Model):
    tipo = models.CharField(max_length=10)

    def __str__(self):
        return self.tipo

class Consumo_carros(models.Model):
    modelos = models.CharField(max_length=50)
    consumo_cidade_etanol = models.CharField(max_length=50, default='')
    consumo_cidade_gasolina = models.CharField(max_length=50, default='')
    consumo_estrada_etanol = models.CharField(max_length=50, default='')
    consumo_estrada_gasolina = models.CharField(max_length=50,default='')

    def __str__(self):
        return self.modelos

class CadCarros(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, default=1)
    veiculo = models.CharField(max_length=50)
    placa = models.CharField(max_length=7)
    ano = models.IntegerField()
    cor = models.CharField(max_length=20)
    tipocombustivel = models.CharField(max_length=10, default='Gasolina')
    marca = models.CharField(max_length=20)
    modelos = models.ForeignKey(Consumo_carros, on_delete=models.DO_NOTHING, default='')

    def __str__(self):
        return self.veiculo