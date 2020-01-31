from rest_framework import viewsets
from .serializers import UserSerializer, CampeonSerializer

from .models import Usuario, Campeon


#Viewset que define el comportamiento de las vistas
class UserViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UserSerializer

class CampeonViewSet(viewsets.ModelViewSet):
    queryset = Campeon.objects.all()
    serializer_class = CampeonSerializer
