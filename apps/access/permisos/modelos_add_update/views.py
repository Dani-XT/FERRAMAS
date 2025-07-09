# Renderizacion Template
from web_project import TemplateLayout
from django.views.generic import TemplateView
from web_project.template_helpers.theme import TemplateHelper

# Modelos
from apps.access.permisos.models import DescripcionContent

# Contribuciones
from apps.access.permisos.helpers import get_permisos_por_modelo
from django.shortcuts import get_object_or_404, redirect
from apps.access.permisos.forms import AddUpdateModeloForm
from django.contrib import messages

# Permisos
from django.contrib.auth.mixins import PermissionRequiredMixin


class ModelosAddUpdateView(PermissionRequiredMixin, TemplateView):
    permission_required = ("auth.view_user")

    def get_context_data(self, **kwargs):
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))
        id_permiso, id_content = get_permisos_por_modelo(self.kwargs['pk'])      

        context.update(
            {
                "id_permiso": id_permiso,
                "id_content": id_content,
            }
        )

        TemplateHelper.map_context(context)
        return context
    
    def post(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk', None)
        instance = get_object_or_404(DescripcionContent, pk=pk)

        form = AddUpdateModeloForm(request.POST, instance=instance)
        if form.is_valid():
            print("Formulario valido")
            messages.success(request, "Modelo actualizado con exito")

        else: 
            print("Formulario no valido")
            messages.error(request, f"Error al crear actualizar {form.errors}")

        return redirect('permisos:modelos-list')

    
    