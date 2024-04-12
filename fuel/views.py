from django.shortcuts import render, redirect
from .models import Combustivel, CadCarros, TipoCombustivel

def abastecimentos(request):
    if not request.user.is_authenticated:
        return redirect('/usuarios/logar/')
    if request.method == "GET":
        combustiveis = Combustivel.objects.all()
        veiculos = CadCarros.objects.all()
        return render(request, 'abastecimentos.html', {'combustivel': combustiveis, 'veiculo': veiculos})


def cad_carros(request):
    if not request.user.is_authenticated:
        return redirect('/usuarios/logar/')
    elif request.method == "GET":
        tipo = TipoCombustivel.objects.all()
        return render(request, 'cad_carros.html', {'tipocombustivel': tipo})
    elif request.method == 'POST':
        veiculo = request.POST.get('veiculo')
        placa = request.POST.get('placa')
        ano = request.POST.get('ano')
        cor = request.POST.get('cor')
        tipocombustivel = request.POST.get('tipocombustivel')
        marca = request.POST.get('marca')
        modelo = request.POST.get('modelo')

    novo_veiculo = CadCarros(
        veiculo = veiculo,
        placa = placa,
        ano = ano,
        cor = cor,
        tipocombustivel = tipocombustivel,
        marca = marca,
        modelo = modelo
    )

    novo_veiculo.save()

    return redirect('/fuel/abastecimentos/')