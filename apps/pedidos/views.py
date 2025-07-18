# Renderizacion Template
from web_project import TemplateLayout
from django.views.generic import TemplateView
from web_project.template_helpers.theme import TemplateHelper

# Permisos
from django.contrib.auth.mixins import PermissionRequiredMixin

# Contrib
from apps.pedidos.helpers import get_all_pedidos

class PedidosView(PermissionRequiredMixin, TemplateView):
    permission_required = ("auth.view_user")

    def get_context_data(self, **kwargs):
        context =  TemplateLayout.init(super().get_context_data(**kwargs))
        pedidos = get_all_pedidos()
        context.update(
            {
                "pedidos": pedidos
            }
        )
        TemplateHelper.map_context(context)
        return context
    