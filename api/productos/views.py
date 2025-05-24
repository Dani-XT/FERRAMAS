from rest_framework import viewsets
# from apps.productos.producto.models import Producto
from apps.front.home.models import Producto
from .serializer import ProductoSerializer

class ProductoApiView(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

    def get(self):
        pass

    def post(self):
        pass

    def delete(self):
        pass

    def put(self):
        pass