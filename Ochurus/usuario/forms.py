from django import forms

from .models import Usuario, Campeon


class RegistrarUsuario(forms.ModelForm):
    class Meta():
        model = Usuario
        help_texts ={
            'username':None,
        }
        fields = ('username','first_name','last_name','password','email','ciudad','telefono')
        labels = {'username':('Usuario'),'first_name':('Nombre'),'last_name':('Apellido'),'password':('Contraseña'),'email':('Correo Electrónico')}
        
class RegistrarCampeon(forms.ModelForm):
    class Meta():
        model = Campeon
        fields = ('nombre','rol','popularidad','porcentaje_victorias','porcentaje_derrotas','imagen','imagen2','imagen3')

        