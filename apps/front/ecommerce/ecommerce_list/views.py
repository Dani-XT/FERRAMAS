# Renderizacion Template
from web_project import TemplateLayout
from django.views.generic import TemplateView
from web_project.template_helpers.theme import TemplateHelper

# Modelos
from apps.front.home.models import Producto

class EcommerceListView(TemplateView):

    def get_context_data(self, **kwargs):
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))
        productos = self.get_all_productos()

        context.update(
            {
                "layout": "front",
                "layout_path": TemplateHelper.set_layout("layout_front.html", context),
                "active_url": self.request.path,  # Get the current url path (active URL) from request
                "productos": productos
            }
        )
        TemplateHelper.map_context(context)
        return context
    
    def get_all_productos(self):
        return Producto.objects.all().order_by('id_producto')
    
   


