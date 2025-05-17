from django.db import models
from django.contrib.auth.models import User
from apps.productos.producto.models import Producto

# Create your models here.
class Review(models.Model):
    producto = models.ForeignKey('Producto', on_delete=models.CASCADE, related_name='reviews')
    usuario = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='reviews')
    calificacion = models.PositiveSmallIntegerField(choices=[(i, str(i)) for i in range(1, 6)])
    comentario = models.TextField(blank=True)
    fecha = models.DateTimeField(auto_now_add=True)

