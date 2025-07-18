from django.urls import path
from django.contrib.auth.decorators import login_required

# Views personalizados
from apps.pedidos.views import PedidosView

urlpatterns = [
    path(
        "pedidos/",
        login_required(PedidosView.as_view(template_name="pedidos_list.html")),
        name="pedidos-list",
    ),
]