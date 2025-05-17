# Renderizacion Template
from web_project import TemplateLayout
from django.views.generic import TemplateView
from web_project.template_helpers.theme import TemplateHelper

# Contribuciones
from django.shortcuts import redirect
from django.contrib import messages

# Permisos
from django.contrib.auth.mixins import PermissionRequiredMixin

# Modelo
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import Group, Permission

# Forms
from apps.access.roles.forms import UpdateRoleForm

# Collections
from collections import defaultdict

class RolesUpdateView(PermissionRequiredMixin, TemplateView):
    permission_required = ("auth.view_user")

    def get_context_data(self, **kwargs):
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))
        rol = self.get_rol(self.kwargs['pk'])
        permisos = self.get_all_permisos()
        permisos_asignados = self.get_all_permisos_asignados(rol)

        context.update(
            {
                "id_rol": rol,
                "permisos": permisos,
                "permisos_asignados": permisos_asignados
            }
        )

        TemplateHelper.map_context(context)
        return context
    
    def get_rol(self, pk):
        return Group.objects.get(pk=pk)
    
    def get_all_permisos(self):
        permisos = Permission.objects.select_related("content_type").all()

        permisos_agrupados = defaultdict(list)
        for permiso in permisos:
            app = permiso.content_type.app_label
            model = permiso.content_type.model
            permisos_agrupados[f"{app}.{model}"].append({
                "id": permiso.id,
                "codename": permiso.codename,
                "name": permiso.name,
            })
        
        orden = ['view', 'add', 'change', 'delete']

        for key, lista in permisos_agrupados.items():
            permisos_agrupados[key] = sorted(
                lista,
                key=lambda x: orden.index(x['codename'].split('_')[0])
            )

        return dict(permisos_agrupados)
    
    def get_all_permisos_asignados(self, grupo):
        return set(grupo.permissions.values_list("id", flat=True))
    
    def post(self, request, pk):
        rol = self.get_rol(pk)
        form = UpdateRoleForm(request.POST, instance=rol)

        if form.is_valid():
            rol.name = form.cleaned_data["rolename"]
            rol.permissions.set(form.cleaned_data["permissions"])
            rol.save()
            messages.success(request, "Grupo actualizado con éxito")
            return redirect("roles-list")
        else:
            messages.error(request, "Hubo un error al actualizar el grupo")
            return redirect("roles-update", pk=rol.pk)

