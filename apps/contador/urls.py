from django.urls import path
from django.contrib.auth.decorators import login_required

# Views personalizados
from apps.contador.views import ContadorView

urlpatterns = [
    path(
        "contador/",
        login_required(ContadorView.as_view(template_name="contador_list.html")),
        name="contador-list",
    )
]