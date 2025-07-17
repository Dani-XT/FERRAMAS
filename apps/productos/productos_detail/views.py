# Renderizacion Template
from web_project import TemplateLayout
from django.views.generic import TemplateView
from web_project.template_helpers.theme import TemplateHelper

# Permisos
from django.contrib.auth.mixins import PermissionRequiredMixin

# Contrib
from apps.productos.helpers import get_producto_detail


class ProductosDetailView(PermissionRequiredMixin, TemplateView):
    permission_required = ("auth.view_user")

    def get_context_data(self, **kwargs):
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))
        pk = self.kwargs.get('pk')
        producto = get_producto_detail(pk)

        context.update(
            {
                "producto": producto
            }
        )
        
        TemplateHelper.map_context(context)
        return context
    
