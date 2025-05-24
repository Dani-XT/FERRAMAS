from rest_framework import viewsets
# from apps.productos.producto.models import Producto
from apps.front.home.models import Producto
from .serializer import ProductoSerializer

class ProductoListAPIView(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer