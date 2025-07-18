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
    path("admin/", include("apps.bodega.urls")),
    path("admin/", include("apps.contador.urls")),
    path("admin/", include("apps.vendedor.urls")),
    # ----------------------------------------
    # Productos
    # ----------------------------------------
    path("admin/", include("apps.productos.urls")),
]