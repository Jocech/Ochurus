from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('base/',views.base,name="base"),
    path('inicio/',views.inicio,name="inicio"),
    path('campeones/',views.campeones,name="campeones"),
    path('registro/',views.registrar,name="registrar"),
]
