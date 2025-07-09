from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.
class Status(models.Model):
    nombre = models.CharField(max_length=150)
    descripcion = models.CharField(max_length=150)

class Producto(models.Model):
    nombre = models.CharField(max_length=250)
    alias = models.CharField(max_length=250)
    descripcion = models.TextField(null=True, blank=True)
    precio = models.IntegerField(validators=[MinValueValidator(0)])
    stock = models.BooleanField(default=True)
    cantidad = models.IntegerField()
    status = models.ForeignKey(Status, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre
    
class Imagen_Producto(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='productos/')
    


