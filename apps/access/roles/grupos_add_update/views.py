# Renderizacion Template
from web_project import TemplateLayout
from django.views.generic import TemplateView
from web_project.template_helpers.theme import TemplateHelper

# Permisos
from django.contrib.auth.mixins import PermissionRequiredMixin

# Contribuciones
from django.shortcuts import redirect
from django.contrib import messages
from apps.access.roles.helpers import get_grupo, get_all_permisos, get_grupo_detail,permisos_seleccionados

# Formularios
from apps.access.roles.forms import AddUpdateGrupoForm

class GruposAddUpdateView(PermissionRequiredMixin, TemplateView):
    permission_required = ("auth.view_user")

    def get_context_data(self, **kwargs):
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))
        pk = self.kwargs.get('pk')
        grupo = get_grupo_detail(pk) if pk else None
        select_perm = permisos_seleccionados(pk) if pk else None

        modelos = get_all_permisos()


        context.update(
            {
                "modelos": modelos,
                "grupo": grupo,
                "select_perm": select_perm
            }
        )
        TemplateHelper.map_context(context)
        return context
    

    def post(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')
        instance = get_grupo(pk) if pk else None
        form = AddUpdateGrupoForm(request.POST, instance=instance)

        if form.is_valid():
            form.save()
            if pk:
                messages.success(request, "Grupo modificado con exito")
            else:
                messages.success(request, "Grupo creado con exito")
        else:
            messages.error(request, f"Error al crear grupo {form.errors}")

        return redirect('roles-list')



