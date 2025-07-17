# RENDERIZACION TEMPLATE
from web_project import TemplateLayout
from django.views.generic import TemplateView
from web_project.template_helpers.theme import TemplateHelper

# PERMISOS
from django.contrib.auth.mixins import PermissionRequiredMixin

# CONTRIB
from apps.usuarios.helpers import get_usuario_detail

class UsuariosDetailView(PermissionRequiredMixin, TemplateView):
    permission_required = ("auth.view_user")

    def get_context_data(self, **kwargs):
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))
        pk = self.kwargs.get('pk')
        usuario = get_usuario_detail(pk)

        context.update(
            {
                "usuario": usuario
            }
        )
        TemplateHelper.map_context(context)
        return context
    