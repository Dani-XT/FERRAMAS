from django.urls import path
from django.contrib.auth.decorators import login_required

# Views personalizados
from apps.productos.producto.productos_list.views import ProductosListView
from apps.productos.producto.productos_add.views import ProductosAddView
from apps.productos.producto.productos_detail.views import ProductosDetailView
from apps.productos.producto.productos_update.views import ProductosUpdateView
from apps.productos.producto.productos_delete.views import ProductosDeleteView

urlpatterns = [
    path(
        "productos/list/",
        login_required(ProductosListView.as_view(template_name="productos_list.html")),
        name="productos-list",
    ),
    path(
        "productos/add/",
        login_required(ProductosAddView.as_view(template_name="productos_add.html")),
        name="productos-add",
    ),
    path(
        "productos/detail/<int:pk>/",
        login_required(ProductosDetailView.as_view(template_name="productos_detail.html")),
        name="productos-detail",
    ),
    path(
        "productos/update/<int:pk>/",
        login_required(ProductosUpdateView.as_view(template_name="productos_update.html")),
        name="productos-update",
    ),
    path(
        "productos/delete/<int:pk>/",
        login_required(ProductosDeleteView.as_view()),
        name="productos-delete",
    ),
]