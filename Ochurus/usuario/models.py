from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Usuario(AbstractUser):
    alias = models.CharField(max_length=10)
    ciudad = models.CharField(max_length=20)
    telefono = models.CharField(max_length=12)
    avatar = models.ImageField(upload_to="avatar",default="default.png")

class Mensajes(models.Model):
    texto = models.CharField(max_length=300)
    usu = models.ForeignKey(Usuario,on_delete=models.CASCADE)

class Campeon(models.Model):
    nombre = models.CharField(max_length=20)
    rol = models.CharField(max_length=10)
    popularidad = models.DecimalField(max_digits=3, decimal_places=2)
    porcentajeVictorias = models.DecimalField(max_digits=3, decimal_places=2)
    porcentajeDerrotas = models.DecimalField(max_digits=3, decimal_places=2)
    votos = models.IntegerField()
    msj = models.ForeignKey(Mensajes,on_delete=models.CASCADE)
   
class ImgCampeon(models.Model):
    nombre = models.CharField(max_length=20)
    url = models.ImageField(upload_to="imgcampeones",default="default.png")


class Item (models.Model):
    nombre = models.CharField(max_length=20)
    url = models.URLField()
