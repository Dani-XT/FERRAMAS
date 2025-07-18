from apps.productos.models import Producto
from django.shortcuts import get_object_or_404, redirect

def get_producto(pk):
    return get_object_or_404(Producto, pk=pk)

def get_producto_detail(pk):
    return get_object_or_404(Producto, pk=pk)

def get_all_productos():
    return Producto.objects.all().order_by('id')