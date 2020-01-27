from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class Usuario(AbstractUser):
    ciudad = models.CharField(max_length=20)
    telefono = models.CharField(max_length=12)
    avatar = models.ImageField(upload_to="avatar",default="default.png")

class Mensajes(models.Model):
    texto = models.CharField(max_length=300)
    usu = models.ForeignKey(Usuario,on_delete=models.CASCADE)

class Campeon(models.Model):
    nombre = models.CharField(max_length=20)
    rol = models.CharField(max_length=10)
    popularidad = models.IntegerField()
    porcentaje_victorias = models.IntegerField()
    porcentaje_derrotas = models.IntegerField()
    imagen = models.ImageField(upload_to="imgcampeon",default="default.png")
    imagen2 = models.ImageField(upload_to="imgcampeon",default="default.png")
    imagen3 = models.ImageField(upload_to="imgcampeon",default="default.png")

class Item(models.Model):
    nombre = models.CharField(max_length=20)
    foto = models.ImageField(upload_to="items",default="default.png")

class ItemCampeon(models.Model):
    camp = models.ForeignKey(Campeon,on_delete=models.CASCADE)
    item = models.ForeignKey(Item,on_delete=models.CASCADE)