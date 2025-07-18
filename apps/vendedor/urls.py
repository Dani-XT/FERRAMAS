from django.urls import path
from django.contrib.auth.decorators import login_required

# Views personalizados
from apps.vendedor.views import VendedorView

urlpatterns = [
    path(
        "vendedor/",
        login_required(VendedorView.as_view(template_name="vendedor_list.html")),
        name="vendedor-list",
    )
]