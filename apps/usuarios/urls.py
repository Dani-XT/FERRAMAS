from django.urls import path
from django.contrib.auth.decorators import login_required

# Views personalizados
from apps.usuarios.views import UsuariosView

from apps.usuarios.usuarios_list.views import UsuariosListView

from apps.usuarios.usuarios_add_update.views import UsuariosAddUpdateView
from apps.usuarios.usuarios_detail.views import UsuariosDetailView
from apps.usuarios.usuarios_delete.views import UsuariosDeleteView

urlpatterns = [
    path(
        "usuarios/list/",
        login_required(UsuariosView.as_view(template_name="usuarios_list.html")),
        name="usuarios-list",
    ),
    path(
        "usuarios/add/",
        login_required(UsuariosAddUpdateView.as_view(template_name="usuarios_add_update.html")),
        name="usuarios-add",
    ),
    path(
        "usuarios/detail/<int:pk>/",
        login_required(UsuariosDetailView.as_view(template_name="usuarios_detail.html")),
        name="usuarios-detail",
    ),
    path(
        "usuarios/update/<int:pk>/",
        login_required(UsuariosAddUpdateView.as_view(template_name="usuarios_add_update.html")),
        name="usuarios-update",
    ),
    path(
        "usuarios/delete/<int:pk>/",
        login_required(UsuariosDeleteView.as_view()),
        name="usuarios-delete",
    ),
]
