# Renderizacion Template
from web_project import TemplateLayout
from django.views.generic import TemplateView
from web_project.template_helpers.theme import TemplateHelper

# Contribuciones
from django.shortcuts import redirect
from django.contrib import messages

# Permisos
from django.contrib.auth.mixins import PermissionRequiredMixin

# Modelos
from django.contrib.auth.models import Group, Permission

# Formularios
from apps.access.roles.forms import AddRoleForm

# Collections
from collections import defaultdict

class RolesAddView(PermissionRequiredMixin, TemplateView):
    permission_required = ("auth.view_user")

    def get_context_data(self, **kwargs):
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))
        permisos = self.get_all_permisos()

        context.update(
            {
                "permisos": permisos,
            }
        )
        TemplateHelper.map_context(context)
        return context
    
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
    
    def post(self, request, *args, **kwargs):
        form = AddRoleForm(request.POST)
        print("antes if forms.is_valid()")
        if form.is_valid():
            print("despues if forms.is_valid()")

            nombre = form.cleaned_data["rolename"]
            permisos = form.cleaned_data["permissions"]

            grupo = Group.objects.create(name=nombre)
            grupo.permissions.set(permisos)
            
            messages.success(request, 'Grupo creado con éxito')
            
            return redirect('roles-list')

        else:
            messages.error(request, 'Error al crear el grupo')
            return redirect('roles-add')

        return redirect('roles-list')


