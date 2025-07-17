from django.contrib.auth.models import Group, User
from django.db.models import Prefetch

# contrib
from django.shortcuts import get_object_or_404

# -----------------------------------------------------
#   Grupos
# -----------------------------------------------------
def get_all_grupos():
    return Group.objects.all().order_by("id")

# -----------------------------------------------------
#   USUARIOS
# -----------------------------------------------------
def get_usuario(pk):
    return User.objects.get(pk=pk)

def get_usuario_detail(pk):
    usuario = get_object_or_404(User, pk=pk)
    grupo = usuario.groups.first()

    return usuario

def get_all_usuarios():
    return User.objects.prefetch_related(
        Prefetch("groups", queryset=Group.objects.only("id", "name"))
    ).all()


