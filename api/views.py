from rest_framework import generics
# from apps.productos.producto.models import Producto
from apps.front.home.models import Producto
from .serializer import ProductoSerializer

class ProductoListAPIView(generics.ListAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer