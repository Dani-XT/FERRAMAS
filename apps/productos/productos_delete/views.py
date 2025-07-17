# Renderizacion Template
from django.views.generic import DeleteView

# Permisos
from django.contrib.auth.mixins import PermissionRequiredMixin

# contribuciones
from django.shortcuts import redirect
from django.contrib import messages
from apps.productos.helpers import get_producto

class ProductosDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = ("auth.view_user")

    def get(self, request, pk):
        producto = get_producto(pk)
        producto.delete()

        messages.success(request, f"El producto {producto.nombre} fue eliminado correctamente")
        return redirect('productos-list')
