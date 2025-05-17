from django.db import models

# Create your models here.
class Status(models.Model):
    nombre = models.CharField(max_length=150)

class Producto(models.Model):
    nombre = models.CharField(max_length=250)
    descripcion = models.TextField(null=True, blank=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.BooleanField(default=True)
    cantidad = models.IntegerField()
    status = models.ForeignKey(Status, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre
    
class Imagen_Producto(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='productos/')
    


