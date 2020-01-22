from rest_framework import serializers
from django.contrib.auth.models import User

#serializer que representa la definición de la API
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['alias','ciudad','telefono','avatar',]