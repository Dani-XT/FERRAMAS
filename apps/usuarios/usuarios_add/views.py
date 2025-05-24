# Renderizacion Template
from web_project import TemplateLayout
from django.views.generic import TemplateView
from web_project.template_helpers.theme import TemplateHelper

# Contrib
from django.shortcuts import redirect
from django.contrib import messages
from apps.usuarios.helpers import get_all_group

# Permisos
from django.contrib.auth.mixins import PermissionRequiredMixin

# Formularios
from apps.usuarios.forms import AddUsuarioForm

class UsuariosAddView(PermissionRequiredMixin, TemplateView):
    permission_required = ("auth.view_user")

    def get_context_data(self, **kwargs):
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))
        grupos = get_all_group()

        context.update(
            {
                "grupos": grupos,
            }
        )
        TemplateHelper.map_context(context)
        return context
    
    def post(self, request):
        form = AddUsuarioForm(request.POST)
        if form.is_valid():
            usuario, password = form.save()
            messages.success(request, f"Usuario creado. Contraseña: {password}")
            return redirect("usuarios-add")
        else:
            messages.error(request, f"Error al crear usuario  {form.errors}")
            return redirect(f"usuarios-add" )
        
            