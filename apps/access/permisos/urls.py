from django.urls import path
from django.contrib.auth.decorators import login_required

# Views personalizados
from apps.access.permisos.views import PermisosViews

from apps.access.permisos.modelos_detail.views import ModelosDetailView
from apps.access.permisos.modelos_add_update.views import ModelosAddUpdateView
from apps.access.permisos.modelos_detail.views import ModelosDetailView
from apps.access.permisos.modelos_delete.views import ModelosDeleteView

urlpatterns = [
    path(
        "access/permisos/",
        login_required(PermisosViews.as_view(template_name="permisos_list.html")),
        name="permisos-list"
    ),
    path(
        "access/permisos/modelos/add/",
        login_required(ModelosAddUpdateView.as_view(template_name="modelos_add.html")),
        name="modelos-add"
    ),
    path(
        "access/permisos/modelos/detail/<int:pk>/",
        login_required(ModelosDetailView.as_view(template_name="modelos_detail.html")),
        name="modelos-detail"
    ),
    path(
        "access/permisos/modelos/update/<int:pk>/",
        login_required(PermisosViews.as_view(template_name="modelos_update.html")),
        name="modelos-update"
    ),
    path(
        "access/permisos/modelos/delete/<int:pk>/",
        login_required(ModelosDeleteView.as_view()),
        name="modelos-delete"
    ),
]
