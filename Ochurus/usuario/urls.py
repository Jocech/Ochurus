from django.contrib import admin
from django.urls import path,include
from . import views

from django.conf import settings
from django.conf.urls.static import static


app_name = "usuario"

urlpatterns = [
    path('',views.index,name="index"),
    path('base/',views.base,name="base"),
    path('inicio/',views.inicio,name="inicio"),
    path('inicio_staff/',views.iniciostaff,name="iniciostaff"),
    path('campeones/',views.campeones,name="campeones"),
    path('registrar/',views.registrar,name="registrar"),
    path('registrar_campeones/',views.registrar_campeones,name="regcampeon"),
    path('cerrarsesion/',views.cerrar_sesion,name="cerrar_sesion"),
    path('subir_items/',views.item,name="item"),
    path('listar/',views.campeon_list,name="listar"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)