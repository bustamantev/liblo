from django.urls import path
from .views import index, categoria1, categoria2, categoria3, categoria4, categoria5, registro, sesion, recuperarcontrasena,modificarperfil

urlpatterns = [
    path('', index,name="index"),
    path('categoria1.html', categoria1,name="categoria1"),
    path('categoria2.html', categoria2,name="categoria2"),
    path('categoria3.html', categoria3,name="categoria3"),   
    path('categoria4.html', categoria4,name="categoria4"),
    path('categoria5.html', categoria5,name="categoria5"),
    path('registro.html', registro,name="registro"),
    path('sesion.html', sesion,name="sesion"),
    path('recuperarcontrasena.html', recuperarcontrasena,name="recuperarcontrasena"),
    path('modificarperfil.html', modificarperfil,name="modificarperfil"),
]
