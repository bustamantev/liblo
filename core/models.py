from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator, MaxLengthValidator, RegexValidator

class Usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nombre_completo = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    direccion = models.CharField(max_length=200)

class ValidacionContrasena(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    longitud_minima = models.PositiveIntegerField(default=8)
    longitud_maxima = models.PositiveIntegerField(default=16)
    caracteres_especiales = models.BooleanField(default=True)
    numeros = models.BooleanField(default=True)
    letras_mayusculas = models.BooleanField(default=True)

    def __str__(self):
        return f"Validación de contraseña para {self.usuario.user.username}"

class ValidacionFormulario(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    nombre_campo = models.CharField(max_length=100)
    validacion_regex = models.CharField(max_length=200, blank=True, null=True)
    validacion_longitud_minima = models.PositiveIntegerField(default=0)
    validacion_longitud_maxima = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"Validación de campo '{self.nombre_campo}' para {self.usuario.user.username}"