from django.urls import path
from django.contrib.auth.decorators import login_required

# Views personalizados
from apps.pedidos.views import PedidosView

from apps.productos.productos_add_update.views import ProductosAddUpdateView
from apps.productos.productos_detail.views import ProductosDetailView
from apps.productos.productos_delete.views import ProductosDeleteView

urlpatterns = [
    path(
        "pedidos/",
        login_required(PedidosView.as_view(template_name="pedidos_list.html")),
        name="pedidos-list",
    ),
]