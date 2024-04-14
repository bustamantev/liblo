from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'core/index.html')

def categoria1(request):
    return render(request, 'core/categoria1.html')

def categoria2(request):
    return render(request, 'core/categoria2.html')

def categoria3(request):
    return render(request, 'core/categoria3.html')

def categoria4(request):
    return render(request, 'core/categoria4.html')

def categoria5(request):
    return render(request, 'core/categoria5.html')

def registro(request):
    return render(request, 'core/registro.html')

def sesion(request):
    return render(request, 'core/sesion.html')

def recuperarcontrasena(request):
    return render(request, 'core/recuperarcontrasena.html')

def modificarperfil(request):
    return render(request, 'core/modificarperfil.html')

