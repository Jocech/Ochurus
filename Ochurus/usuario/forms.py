from django import forms

from .models import Usuario, Campeon


class RegistrarUsuario(forms.ModelForm):
    class Meta():
        model = Usuario
        fields = ('username','first_name','last_name','password','email','ciudad','telefono')

class RegistrarCampeon(forms.ModelForm):
    class Meta():
        model = Campeon
        fields = ('nombre','rol','popularidad','porcentaje_victorias','porcentaje_derrotas')

        