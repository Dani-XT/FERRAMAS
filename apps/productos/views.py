# Renderizacion Template
from web_project import TemplateLayout
from django.views.generic import TemplateView
from web_project.template_helpers.theme import TemplateHelper

# Permisos
from django.contrib.auth.mixins import PermissionRequiredMixin

# contrib
from apps.productos.helpers import get_all_productos

class ProductosView(PermissionRequiredMixin, TemplateView):
    permission_required = ("auth.view_user")

    def get_context_data(self, **kwargs):
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))
        productos = get_all_productos()

        context.update(
            {
                "productos": productos,
            }
        )

        TemplateHelper.map_context(context)
        return context
    
