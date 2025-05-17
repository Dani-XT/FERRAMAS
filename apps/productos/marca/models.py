from django.db import models
from apps.productos.producto.models import Producto

# Create your models here.
class Marca(models.Model):
    nombre = models.CharField(max_length=250)
    nombre_completo = models.TextField()
    descripcion = models.TextField()

class Producto_Marca(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)