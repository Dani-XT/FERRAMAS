from django.db import models

# models
from apps.ventas.models import Venta
from django.contrib.auth.models import User

# Create your models here.
class EstadoPedido(models.Model):
    nombre = models.CharField(max_length=150)
    descripcion = models.CharField(max_length=200, blank=True, null=True)

class PedidoManager(models.Manager):
    def por_estado(self, nombre_estado):
        return self.filter(estado__nombre__iexact=nombre_estado)

class Pedido(models.Model):
    venta = models.OneToOneField(Venta, on_delete=models.CASCADE, related_name='pedido')
    estado = models.ForeignKey(EstadoPedido, on_delete=models.CASCADE, related_name='pedidos')

    date_created = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)
    fecha_entrega = models.DateTimeField(null=True, blank=True)
    entregado_por = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name="pedidos_entregados")

    objects = PedidoManager()

    @property
    def es_entregado(self):
        return self.estado.nombre.lower() == 'entregado'



