from django.db import models

# Create your models here.
class Producto(models.Model):
    nombre = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=300)
    precio = models.FloatField(default=10)
    stock = models.IntegerField()
    imagen = models.CharField(max_length=40)
    
    def __str__(self):
        return self.nombre

class Carrito(models.Model):
    producto = models.CharField(max_length=30)
    usuario = models.CharField(max_length=30)
    cantidad = models.IntegerField()

class Usuario(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=15)

    def __str__(self):
        return self.username


