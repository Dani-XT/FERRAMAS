# Renderizacion Template
from web_project import TemplateLayout
from django.views.generic import TemplateView
from web_project.template_helpers.theme import TemplateHelper

# Permisos
from django.contrib.auth.mixins import PermissionRequiredMixin

# utils
from apps.core.helpers import get_all_comunas, get_all_regiones, get_all_provincias


class CoreView(PermissionRequiredMixin, TemplateView):
    permission_required = ("auth.view_user")

    def get_context_data(self, **kwargs):
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))
        comunas = get_all_comunas()
        regiones = get_all_regiones()
        provincias = get_all_provincias()

        context.update(
            {
                "comunas": comunas,
                "regiones": regiones,
                "provincias": provincias
            }
        )
        
        TemplateHelper.map_context(context)
        return context
    
