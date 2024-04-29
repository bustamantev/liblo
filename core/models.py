from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

<<<<<<< HEAD

class CustomUser(AbstractUser):
    birth_date = models.DateField(blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True)
    address = models.CharField(max_length=100, blank=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    def _str_(self):
        return self

class CategoriaLibro(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre


class Libro(models.Model):
    categoria = models.ForeignKey(CategoriaLibro, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    # hecho CharField por problemas al formatear con las template tags en django
    precio = models.CharField(max_length=10)
    src_imagen = models.URLField(blank=True, null=True)
=======
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
>>>>>>> da007479b86306d610970e752d172c7b3ad0e87a

    def __str__(self):
        return self.titulo





