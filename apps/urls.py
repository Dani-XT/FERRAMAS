from django.urls import path, include

urlpatterns = [
    path("admin/", include("apps.home.urls")),
    # ----------------------------------------
    # Sistema
    # ----------------------------------------
    path("admin/", include("apps.access.roles.urls")),
    path("admin/", include("apps.access.permisos.urls")),
    path("admin/", include("apps.usuarios.urls")),
    path("admin/", include("apps.core.urls")),
    path("admin/", include("apps.ventas.urls")),
    path("admin/", include("apps.pedidos.urls")),
    # ----------------------------------------
    # Productos
    # ----------------------------------------
    path("admin/", include("apps.productos.urls")),
    # ----------------------------------------
    # Cuenta
    # ----------------------------------------
    path("admin/", include("apps.accounts.urls")),
]