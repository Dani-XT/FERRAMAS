from django.urls import path
from django.contrib.auth.decorators import login_required

# Views personalizados
from apps.productos.views import ProductosView

from apps.productos.productos_add_update.views import ProductosAddUpdateView
from apps.productos.productos_detail.views import ProductosDetailView
from apps.productos.productos_delete.views import ProductosDeleteView

urlpatterns = [
    path(
        "productos/list/",
        login_required(ProductosView.as_view(template_name="productos_list.html")),
        name="productos-list",
    ),
    path(
        "productos/add/",
        login_required(ProductosAddUpdateView.as_view(template_name="productos_add_update.html")),
        name="productos-add",
    ),
    path(
        "productos/detail/<int:pk>/",
        login_required(ProductosDetailView.as_view(template_name="productos_detail.html")),
        name="productos-detail",
    ),
    path(
        "productos/update/<int:pk>/",
        login_required(ProductosAddUpdateView.as_view(template_name="productos_add_update.html")),
        name="productos-update",
    ),
    path(
        "productos/delete/<int:pk>/",
        login_required(ProductosDeleteView.as_view()),
        name="productos-delete",
    ),
]