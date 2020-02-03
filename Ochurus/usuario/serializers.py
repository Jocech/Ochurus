from rest_framework import serializers

from .models import Usuario, Campeon
#serializer que representa la definición de la API
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Usuario
        fields = ['username','ciudad','telefono','avatar','last_name','email','first_name','password']

class CampeonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Campeon
        fields = ['nombre','rol','popularidad','porcentaje_victorias','porcentaje_derrotas','imagen','imagen2','imagen3']