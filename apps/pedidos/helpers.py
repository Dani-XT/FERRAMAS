from apps.pedidos.models import Pedido

# contrib
from django.shortcuts import get_object_or_404

def get_pedido(pk):
    return get_object_or_404(Pedido, pk=pk)

def get_pedido_detail(pk):
    return get_object_or_404(Pedido, pk=pk)

def get_all_pedidos():
    return Pedido.objects.all().order_by('id')