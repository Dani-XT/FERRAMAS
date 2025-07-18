from django.db import models
from django.core.validators import MinValueValidator

#modelo
from front.ecommerce.models import Carrito
from django.contrib.auth.models import User

# Create your models here.
class MedioPago(models.Model):
    nombre = models.CharField(max_length=150)
    descripcion = models.CharField(max_length=200, blank=True, null=True)


class Venta(models.Model):
    carrito = models.OneToOneField(Carrito, on_delete=models.CASCADE, related_name='venta')
    cliente = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ventas')
    
    date_created = models.DateTimeField(auto_now_add=True)
    total = models.IntegerField(validators=[MinValueValidator(0)])
    medio_pago = models.ForeignKey(MedioPago, on_delete=models.CASCADE, related_name='ventas')
    confirmada = models.BooleanField(default=False)


