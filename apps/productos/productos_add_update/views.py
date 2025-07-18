# Renderizacion Template
from web_project import TemplateLayout
from django.views.generic import TemplateView
from web_project.template_helpers.theme import TemplateHelper
from django.shortcuts import redirect

# Permisos
from django.contrib.auth.mixins import PermissionRequiredMixin

# Contrib
from django.contrib import messages
from apps.productos.helpers import get_producto, get_all_estados
from apps.productos.forms import ProductoAddUpdateForm


class ProductosAddUpdateView(PermissionRequiredMixin, TemplateView):
    permission_required = ("auth.view_user")

    def get_context_data(self, **kwargs):
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))
        pk = self.kwargs.get('pk')

        producto = get_producto(pk) if pk else None
        estados = get_all_estados()

        context.update(
            {
                "estados": estados,
                "producto": producto,
            }
        )
        
        TemplateHelper.map_context(context)
        return context
    
    def post(self, request, *args, **kwargs):
        if self.request.method == "POST":
            pk = self.kwargs.get('pk')
            producto = get_producto(pk) if pk else None

            form = ProductoAddUpdateForm(request.POST, request.FILES, instance=producto)
            if form.is_valid():
                form.save()
                messages.success(request, f'Exito')
            else:
                messages.error(request, f'Error {form.errors}')

            return redirect('productos-list')
