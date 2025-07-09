from django.urls import path
from django.contrib.auth.decorators import login_required

# Views personalizados
from apps.access.roles.views import RolesView

from apps.access.roles.grupos_add_update.views import GruposAddUpdateView
from apps.access.roles.grupos_delete.views import GruposDeleteView
from apps.access.roles.grupos_detail.views import GruposDetailView

urlpatterns = [
    path(
        "access/roles/",
        login_required(RolesView.as_view(template_name="roles_list.html")),
        name="roles-list",
    ),
    path(
        "access/roles/grupos/add/",
        login_required(GruposAddUpdateView.as_view(template_name="grupos_add_update.html")),
        name="grupos-add"
    ),
    path(
        "access/roles/grupos/detail/<int:pk>/",
        login_required(GruposDetailView.as_view(template_name="grupos_add_update.html")),
        name="grupos-detail"
    ),
    path(
        "access/roles/grupos/update/<int:pk>/",
        login_required(GruposAddUpdateView.as_view(template_name="grupos_add_update.html")),
        name="grupos-update"
    ),
    path(
        "access/roles/grupos/delete/<int:pk>/",
        login_required(GruposDeleteView.as_view()),
        name="grupos-delete"
    )
]
