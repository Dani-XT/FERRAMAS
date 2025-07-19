from django.db import models
from django.core.validators import MinValueValidator

from apps.productos.models import Producto
from django.contrib.auth.models import User

# Create your models here.
class Carrito(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name="carritos")
    producto = models.ManyToManyField(Producto, through='ItemCarrito', related_name="carritos")
    
    date_created = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)
    total_items = models.IntegerField(validators=[MinValueValidator(1)])
    total = models.IntegerField(validators=[MinValueValidator(0)])

    def __str__(self):
        return f'Carrito: {self.usuario.username} - {self.date_created}'

class ItemCarrito(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name="items_carrito")
    carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE, related_name="items")
    
    cantidad = models.IntegerField(validators=[MinValueValidator(1)])
    date_created = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('carrito', 'producto')

    def __str__(self):
        return f'Item: {self.carrito}: {self.cantidad}'



