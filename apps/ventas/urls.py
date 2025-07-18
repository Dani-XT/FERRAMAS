from django.urls import path
from django.contrib.auth.decorators import login_required

# Views personalizados
from apps.ventas.views import VentasView

urlpatterns = [
    path(
        "ventas/",
        login_required(VentasView.as_view(template_name="ventas_list.html")),
        name="ventas-list",
    ),
]