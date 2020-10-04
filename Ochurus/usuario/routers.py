from .viewsets import UserViewSet, CampeonViewSet
from rest_framework import routers

#los routers proveen una manera fácil de determinar la configuracion URL
router = routers.DefaultRouter()
router.register(r'usuarios',UserViewSet,basename='user')
router.register(r'campeones',CampeonViewSet,basename='campeones')