# Renderizacion Template
from web_project import TemplateLayout
from django.views.generic import TemplateView
from web_project.template_helpers.theme import TemplateHelper

# Permisos
from django.contrib.auth.mixins import PermissionRequiredMixin

# contrib
from apps.ventas.helpers import get_all_ventas

class VentasView(PermissionRequiredMixin, TemplateView):
    permission_required = ("auth.view_user")

    def get_context_data(self, **kwargs):
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))
        ventas = get_all_ventas()

        context.update(
            {
                "ventas": ventas,
            }
        )

        TemplateHelper.map_context(context)
        return context