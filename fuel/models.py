from django.db import models

class Combustivel(models.Model):
    nome = models.CharField(max_length=30)

    def __str__(self):
        return self.nome


class Abastecimento(models.Model):
    COMBUSTIVEL_CHOICES = (('G', 'Gasolina'), ('E', 'Etanol'), ('D', 'Diesel'))
    data_abastecimento = models.DateField()
    combustivel = models.CharField(max_length=1, choices=COMBUSTIVEL_CHOICES)
    km_inicial = models.CharField(max_length=10)
    km_final = models.CharField(max_length=10)
    km_rodado = models.CharField(max_length=10)
    litros_abastecidos = models.CharField(max_length=5)
    custo_total = models.CharField(max_length=7)
    custo_litro = models.CharField(max_length=5)
    km_litro = models.CharField(max_length=5)
    custo_km = models.CharField(max_length=5)

    def __str__(self):
        return self.combustivel

class TipoCombustivel(models.Model):
    tipo = models.CharField(max_length=10)

    def __str__(self):
        return self.tipo

class CadCarros(models.Model):
    veiculo = models.CharField(max_length=50)
    placa = models.CharField(max_length=7)
    ano = models.IntegerField(max_length=4)
    cor = models.CharField(max_length=20)
    tipocombustivel = models.CharField(max_length=10, default='Gasolina')
    marca = models.CharField(max_length=20)
    modelo = models.CharField(max_length=20)

    def __str__(self):
        return self.veiculo