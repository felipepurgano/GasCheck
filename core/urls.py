from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('usuarios/', include('usuarios.urls')),
    path('fuel/', include('fuel.urls')),
    path('dicas/', include('dicas.urls')),
]
