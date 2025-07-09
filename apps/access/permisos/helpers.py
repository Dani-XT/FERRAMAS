from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from collections import defaultdict
from itertools import chain
from django.shortcuts import get_object_or_404
from apps.access.permisos.models import DescripcionContent, DescripcionPermiso
from apps.access.roles.models import DescripcionGrupo

# -------------------------------------------------------
# TODO: MODELOS
# -------------------------------------------------------
def get_all_modelos():
    """
    Retorna todos los modelos que existen en el Programa y sus grupos asociados
    """
    content_types = ContentType.objects.prefetch_related('permission_set__group_set').all()
    desc_modelos = []

    for content in content_types:
        desc_content, _ = DescripcionContent.objects.get_or_create(content=content)
        desc_grupos = []

        for permiso in content.permission_set.all():
            for grupo in permiso.group_set.all():
                desc_grupo, _ = DescripcionGrupo.objects.get_or_create(grupo=grupo)
                desc_grupos.append({
                    "id": grupo.id,
                    "nombre": grupo.name,
                    "bg_color": desc_grupo.bg_color
                })

        desc_modelos.append({
            "id": content.id,
            "app": desc_content.app,
            "modelo": desc_content.modelo,
            "fecha": desc_content.date_created,
            "grupos": desc_grupos
        })

    return desc_modelos


def get_permisos_por_modelo(content_type_id):
    """
    Obtiene el detalle del modelo junto sus permisos
    """
    content_type = get_object_or_404(ContentType, id=content_type_id)

    permisos = (
        Permission.objects
        .filter(content_type=content_type)
        .prefetch_related('group_set')
        .order_by("codename")
    )

    permisos_con_grupos = []
    for permiso in permisos:
        grupos = list(permiso.group_set.values("id", "name"))
        desc_permiso, created = DescripcionPermiso.objects.get_or_create(permiso=permiso)

        permisos_con_grupos.append({
            "id": permiso.id,
            "name": permiso.name,
            "codename": permiso.codename,
            "descripcion": desc_permiso.descripcion,
            "bg_color": desc_permiso.bg_color,
            "icono": desc_permiso.icono,
            "date_created": desc_permiso.date_created,
            "grupos": grupos
        })

    desc_content, created = DescripcionContent.objects.get_or_create(content = content_type)
    
    return permisos_con_grupos, {
        "id": content_type.id,
        "app_label": content_type.app_label,
        "model": content_type.model,
        "nombre": desc_content.app,
        "modelo": desc_content.modelo,
        "descripcion": desc_content.descripcion,
        "icono": desc_content.icono,
        "bg_color": desc_content.bg_color,
        "date_created": desc_content.date_created,
    }

def get_detail_permiso(pk):
    permiso = get_object_or_404(Permission, pk=pk)
    desc_permiso, created = DescripcionPermiso.objects.get_or_create(permiso=permiso)

    grupos = list(permiso.group_set.values("id", "name"))

    return {
        "id": permiso.id,
        "name": permiso.name,
        "codename": permiso.codename,
        "app_label": permiso.content_type.app_label,
        "model": permiso.content_type.model,
        "description": desc_permiso.descripcion,
        "bg_color": desc_permiso.bg_color,
        "icon": desc_permiso.icono,
        "date_created": desc_permiso.date_created,
        "grupos": grupos,
    }
