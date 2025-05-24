# Renderizacion Template
from web_project import TemplateLayout
from django.views.generic import TemplateView
from web_project.template_helpers.theme import TemplateHelper

# Permisos
from django.contrib.auth.mixins import PermissionRequiredMixin

# Contrib
from apps.usuarios.helpers import get_user, get_group, get_all_group
from django.shortcuts import redirect
from django.contrib import messages

# Forms
from apps.usuarios.forms import UpdateUsuarioForm

class UsuariosUpdateView(PermissionRequiredMixin, TemplateView):
    permission_required = ("auth.view_user")

    def get_context_data(self, **kwargs):
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))
        
        usuario = get_user(self.kwargs['pk'])
        grupo_usuario = get_group(usuario)


        grupos = get_all_group()

        context.update(
            {
                "id_usuario": usuario,
                "grupo_usuario": grupo_usuario,
                "grupos": grupos,
            }
        )

        TemplateHelper.map_context(context)
        return context
    
    def post(self, request, pk):
        usuario = get_user(pk)

        form = UpdateUsuarioForm(request.POST, usuario=usuario)

        if form.is_valid():
            form.save()
            messages.success(request, "Usuario actualizado correctamente")

        else:
            messages.error(request, f"Error al actualizar usuario: {form.errors}")
            return redirect('usuarios-update', pk=usuario.pk)

        return redirect('usuarios-list')
        