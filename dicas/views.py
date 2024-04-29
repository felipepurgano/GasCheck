from django.shortcuts import render, HttpResponse


def dicas(request):
    return render(request, 'dicas.html')

