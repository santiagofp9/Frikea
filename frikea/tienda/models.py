from django.db import models

# Create your models here.

class Usuario(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=15)

    def __str__(self):
        return self.username

class Categoria(models.Model):
    nombre = models.CharField(max_length=30)
    
    def __str__(self):
        return self.nombre
      
class Producto(models.Model):
    nombre = models.CharField(max_length=30)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, null=True)
    descripcion = models.TextField(max_length=300)
    precio = models.DecimalField(decimal_places=2, max_digits=6)
    stock = models.IntegerField()
    imagen = models.ImageField(upload_to = 'static/iemeges/')

    def __str__(self):
        return self.nombre

class Carrito(models.Model):
    producto = models.ForeignKey(Producto, on_delete= models.CASCADE, null=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, null=True)
    cantidad = models.IntegerField()
