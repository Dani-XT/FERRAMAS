from apps.productos.models import Producto, Status
from django.shortcuts import get_object_or_404

def get_all_estados():
    return Status.objects.all().order_by('id') 

def get_producto(pk):
    return get_object_or_404(Producto, pk=pk)

def get_all_productos():
    return Producto.objects.all().order_by('id')

def get_producto_detail(pk):
    return get_object_or_404(Producto, pk=pk)