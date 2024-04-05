from django.shortcuts import render, HttpResponse

def abastecimentos(request):
    return render(request, 'abastecimentos.html')

def cad_carros(request):
    return render(request, 'cad_carros.html')