from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name="index"),
    path('historia/', historia, name="historia"),
    path('fantasia/', fantasia, name="fantasia"),
    path('manuales/', manuales, name="manuales"),   
    path('novelas/', novelas, name="novelas"),
    path('psicologia/', psicologia, name="psicologia"),
    path('registro/', registro, name="registro"),
    path('sesion/', sesion, name="sesion"),
    path('recuperacion/', recuperacion, name="recuperacion"),
    path('modificacion/', modificacion, name="modificacion"),
    
]
