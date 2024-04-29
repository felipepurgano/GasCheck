from django.urls import path
from . import views

urlpatterns = [
    path('dicas/', views.dicas, name='dicas'),
]