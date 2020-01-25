from django.contrib import admin
from django.urls import path,include
from . import views
app_name = "usuario"

urlpatterns = [
    path('',views.index,name="index"),
    path('base/',views.base,name="base"),
    path('inicio/',views.inicio,name="inicio"),
    path('campeones/',views.campeones,name="campeones"),
    path('registrar/',views.registrar,name="registrar"),
    path('registrar_staff/',views.registrar_staff,name="regstaff"),
    path('cerrarsesion/',views.cerrar_sesion,name="cerrar_sesion"),
]
