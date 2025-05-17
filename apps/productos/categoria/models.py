from django.db import models
from apps.productos.producto.models import Producto

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=250)
    descripcion = models.TextField()

class Producto_Categoria(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)