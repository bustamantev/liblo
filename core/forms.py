from django import forms
from .models import Perfil

class RegistroFormulario(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ['nombre_completo', 'fecha_nacimiento', 'nombre_usuario', 'email', 'contrasena', 'direccion']
