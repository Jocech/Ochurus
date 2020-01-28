from .viewsets import UserViewSet
from rest_framework import routers

#los routers proveen una manera fácil de determinar la configuracion URL
router = routers.DefaultRouter()
router.register('users',UserViewSet)