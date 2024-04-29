from django.db import models
from django.contrib.auth.models import User

class Perfil(models.Model):
    nombre_completo = models.CharField(max_length=200, default='')  # Campo para nombre y apellido combinados
    fecha_nacimiento = models.DateField(null=True, blank=True)
    nombre_usuario = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    contrasena = models.CharField(max_length=128)
    direccion = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.nombre_completo
    
class RecuperacionContrasena(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=100)
    fecha_expiracion = models.DateTimeField()
    usado = models.BooleanField(default=False)

    def __str__(self):
        return f"Token para {self.usuario.username}"