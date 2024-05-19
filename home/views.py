from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def dicas(request):
    return render(request, 'dicas.html')