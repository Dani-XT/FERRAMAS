from rest_framework import serializers
# from apps.productos.producto.models import Producto
from apps.front.home.models import Producto

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'