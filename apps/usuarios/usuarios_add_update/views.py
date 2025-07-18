# RENDERIZACION TEMPLATE
from web_project import TemplateLayout
from django.views.generic import TemplateView
from web_project.template_helpers.theme import TemplateHelper

# Permisos
from django.contrib.auth.mixins import PermissionRequiredMixin

# Contrib
from django.shortcuts import redirect
from django.contrib import messages
from apps.usuarios.helpers import get_usuario, get_all_grupos
from apps.usuarios.forms import UsuarioAddUpdateForm

class UsuariosAddUpdateView(PermissionRequiredMixin, TemplateView):
    permission_required = ("auth.view_user")

    def get_context_data(self, **kwargs):
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))
        pk = self.kwargs.get('pk')
        usuario = get_usuario(pk) if pk else None
        grupos = get_all_grupos()

        context.update(
            {
                "usuario": usuario,
                "grupos": grupos,
            }
        )
        TemplateHelper.map_context(context)
        return context
    
    def post(self, request, *args, **kwargs):
        if self.request.method == "POST":
            pk = self.kwargs.get('pk')
            usuario = get_usuario(pk) if pk else None

            form = UsuarioAddUpdateForm(request.POST, instance=usuario)
            if form.is_valid():
                usuario, contraseña = form.save()
                if contraseña:
                    messages.success(request, f'Usuario {usuario.username} creado con éxito. Contraseña: {contraseña}')
                else:
                    messages.success(request, f'Usuario {usuario.username} modificado con éxito.')
            else:
                messages.error(request, f'Error {form.errors}')

        return redirect('usuarios-list')
    