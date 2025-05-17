from django.urls import path
from django.contrib.auth.decorators import login_required

# Views personalizados
from apps.admin_home.views import HomeAdminView

urlpatterns = [
    path(
        "home/",
        login_required(HomeAdminView.as_view(template_name="admin_home.html")),
        name="admin-home",
    ),
]