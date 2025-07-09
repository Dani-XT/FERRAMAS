from django.urls import path
from django.contrib.auth.decorators import login_required

# Views personalizados
from apps.core.views import CoreView

urlpatterns = [
   path(
        "core/",
        login_required(CoreView.as_view(template_name="core_home.html")),
        name="core-home",
    ),
]