from django.shortcuts import render, redirect
from .models import Combustivel, CadCarros, TipoCombustivel, Abastecimento
from django.contrib.messages import constants
from django.contrib import messages
from datetime import datetime

def abastecimentos(request):
    if not request.user.is_authenticated:
        return redirect('/usuarios/logar/')
    if request.method == 'GET':
        combustiveis = Combustivel.objects.all()
        veiculos = CadCarros.objects.filter(user=request.user) 
        data_abastecimento = Abastecimento.objects.filter(user=request.user)

        veiculo_filtrar = request.GET.get("veiculo")
        data_abast_filtrar = request.GET.get("data_abastecimento")

        #Os dois if's abaixo são responsáveis por realizar os filtros da datas de abastecimentos
        if veiculo_filtrar:
            veiculo = CadCarros.objects.filter(veiculo=veiculo_filtrar)
                
        if data_abast_filtrar:
            # Converta a string da data para um objeto datetime, se necessário
            data_abast_filtrar_dt = datetime.strptime(data_abast_filtrar, '%Y-%m-%d')
            data_abastecimento = data_abastecimento.filter(data_abastecimento=data_abast_filtrar_dt)

        #A variável abaixo retorna os dados que foram armazenados no banco e fazem o cálculo da diferença dos Km rodados.
        litros_abastecidos = Abastecimento.objects.filter(user=request.user)
        custo_total = Abastecimento.objects.filter(user=request.user)
        km_rodados = ""
        media = ""
        custo_km = ""
        custo_abastecimento = ""

        if data_abast_filtrar:
            for resultado in data_abastecimento:
                diferenca = resultado.km_final - resultado.km_inicial
                km_rodados = (f"Diferença KM: {diferenca}")
                break
        else:
            km_rodados = ("Diferença KM: Nenhhum filtro aplicado")

        if data_abast_filtrar:
            for media in data_abastecimento:  # Filtra resultados para 'media'
                litros = litros_abastecidos.filter(user=request.user).first().litros_abastecidos
                media_km = (media.km_final - media.km_inicial) / litros
                media = (f"Média de KM/Litro: {media_km:.2f}")
            for custo_litro in data_abastecimento:  # Filtra resultados para 'custo_litro'
                custo_lt = custo_litro.custo_total / custo_litro.litros_abastecidos
                custo_litro = (f"Custo por litro: R${custo_lt:.2f}")
            for custo_km in data_abastecimento:  # Filtra resultados para 'custo_km'
                custo = custo_total.filter(user=request.user).first().custo_total
                cust_km = custo / (custo_km.km_final - custo_km.km_inicial)
                custo_km = (f"Custo por KM: R${cust_km:.2f}")
            for custo_abastecimento in data_abastecimento:  # Filtra resultados para 'custo_abastecimento'
                custo_t = custo_total.filter(user=request.user).first().custo_total
                custo_abastecimento = (f"Custo Total: R${custo_t}")
        else:
            media = "Média de KM/Litro: Nenhum filtro aplicado."
            custo_litro = "Custo por litro: Nenhum filtro aplicado."
            custo_km = "Custo por KM: Nenhum filtro aplicado."
            custo_abastecimento = "Custo Total: Nenhum filtro aplicado."

        return render(request, 'abastecimentos.html', {'combustivel': combustiveis, 'veiculo': veiculos, 'data_abastecimento': data_abastecimento, 
                                                        'km_rodados': km_rodados, 'media': media, 'custo_litro': custo_litro, "custo_km": custo_km, "custo_abastecimento": custo_abastecimento})
    
    elif request.method == 'POST':
        veiculo = request.POST.get('veiculo')
        data_abastecimento = request.POST.get('data_abastecimento')
        combustivel = request.POST.get('combustivel')
        posto = request.POST.get('posto')
        litros_abastecidos = request.POST.get('litros_abastecidos')
        km_inicial = request.POST.get('km_inicial')
        km_final = request.POST.get('km_final')
        custo_total = request.POST.get('custo_total')

    novo_abastecimento = Abastecimento(
        user=request.user,
        veiculo=veiculo,
        data_abastecimento=data_abastecimento,
        combustivel=combustivel,
        posto=posto,
        litros_abastecidos=litros_abastecidos,
        km_inicial=km_inicial,
        km_final=km_final,
        custo_total=custo_total
    )

    novo_abastecimento.save()

    messages.add_message(request, constants.SUCCESS, 'Abastecimento cadastrado com sucesso')
    return redirect('/fuel/abastecimentos/')

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
        user=request.user,
        veiculo = veiculo,
        placa = placa,
        ano = ano,
        cor = cor,
        tipocombustivel = tipocombustivel,
        marca = marca,
        modelo = modelo
    )

    novo_veiculo.save()

    messages.add_message(request, constants.SUCCESS, 'Carro cadastrado com sucesso')
    return redirect('/fuel/abastecimentos/')

#TODO: Colocar um filtro para exibir o KM_INICIAL e KM_FINAL na momento de filtrar os dados dos abastecimentos