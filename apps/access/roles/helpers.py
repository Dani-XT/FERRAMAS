# Contrib
from collections import defaultdict
from django.shortcuts import get_object_or_404

# Modelos
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import Permission
from django.contrib.auth.models import Group, User
from apps.access.permisos.models import DescripcionContent, DescripcionPermiso
from apps.access.roles.models import DescripcionGrupo

# -------------------------------------------------------
# TODO: MODELOS
# -------------------------------------------------------
def get_grupo(pk):
    """ Retorna si existe un grupo o no """
    return get_object_or_404(Group, pk=pk)

def get_grupo_detail(pk):
    """ Obtiene el Grupo con sus detalles """
    grupo = get_object_or_404(Group, pk=pk)
    desc_grupo, _ = DescripcionGrupo.objects.get_or_create(grupo=grupo)

    return {
        "id": grupo.id,
        "nombre": grupo.name,
        "descripcion": desc_grupo.descripcion,
        "bg_color": desc_grupo.bg_color,
        "icono": desc_grupo.icono,
        "date_created": desc_grupo.date_created,
    }

def get_all_grupos():
    """ Obtiene todos los grupos asociados al sistema """
    grupos = Group.objects.all().order_by('id')

    grupos_totales = []

    for grupo in grupos:
        desc_grupo, _ = DescripcionGrupo.objects.get_or_create(grupo=grupo)
        usuarios = grupo.user_set.all()
        grupos_totales.append({
            "id": grupo.id,
            "nombre": grupo.name,
            "descripcion": desc_grupo.descripcion,
            "bg_color": desc_grupo.bg_color,
            "icono": desc_grupo.icono,
            "date_created": desc_grupo.date_created,
            "usuarios": usuarios,
            "total": usuarios.count()
        })
    
    return grupos_totales

def get_all_permisos():
    content_types = ContentType.objects.select_related("descripcion_content").prefetch_related("permission_set").all()
    modelos_permisos = []
    for content in content_types:
        
        try:
            desc_content = content.descripcion_content

        except DescripcionContent.DoesNotExist:
            desc_content = DescripcionContent.objects.create(content=content)

        desc_permisos = []

        for permiso in content.permission_set.all():
            desc_permisos.append({
                "id": permiso.id,
                "nombre": permiso.name,
                "codename": permiso.codename
            })
        modelos_permisos.append({
            "id": desc_content.content.id,
            "app": desc_content.app,
            "modelo": desc_content.modelo,
            "permisos": desc_permisos
        })
    
    return modelos_permisos

def permisos_seleccionados(pk):
    grupo = Group.objects.get(pk=pk)
    permisos_asignados = list(grupo.permissions.all().values_list("id", flat=True))
    print(permisos_asignados)
    return permisos_asignados