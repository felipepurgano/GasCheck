from django.urls import path
from . import views

urlpatterns = [
    path('abastecimentos/', views.abastecimentos, name='abastecimentos'),
    path('cad_carros/', views.cad_carros, name='cad_carros'),
]