from django.urls import path
from django.contrib.auth.decorators import login_required

# Views personalizados
from apps.bodega.views import BodegaView

urlpatterns = [
    path(
        "bodega/",
        login_required(BodegaView.as_view(template_name="bodega_list.html")),
        name="bodega-list",
    )
]