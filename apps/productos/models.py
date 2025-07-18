from django.db import models
from django.core.validators import MinValueValidator
from PIL import Image
from apps.utils.utils import nombre_imagen

from django.contrib.auth.models import User

# Create your models here.
class Status(models.Model):
    nombre = models.CharField(max_length=150)
    descripcion = models.CharField(max_length=150)

class Producto(models.Model):
    status = models.ForeignKey(Status, on_delete=models.CASCADE, related_name="productos")
    
    nombre = models.CharField(max_length=250)
    alias = models.CharField(max_length=250)
    descripcion = models.TextField(null=True, blank=True)
    precio = models.IntegerField(validators=[MinValueValidator(0)])
    stock = models.BooleanField(default=True)
    cantidad = models.IntegerField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre
    
class ImagenProducto(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name='imagenes')
    imagen = models.ImageField(upload_to='productos/')

    

class Pedido(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name="pedidos")


class EstadoPedido(models.Model):
    nombre = models.CharField(max_length=150)
    descripcion = models.CharField(max_length=150)

            

