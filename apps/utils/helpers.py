
from apps.utils.models import Comuna, Provincia, Region
from django.shortcuts import get_object_or_404
from django.utils import timezone

from datetime import timedelta


from apps.utils.models import Comuna, Provincia, Region
from apps.access.permisos.models import DescripcionContent, DescripcionPermiso
from apps.utils.models import ValorSistema

from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import Group, Permission

from django.shortcuts import get_object_or_404
from django.urls import reverse

# -------------------------------------------------------
# TODO: HELPERS
# -------------------------------------------------------
def get_unidad_duracion():
    return ValorSistema.objects.filter(grupo__nombre="tiempo", is_plural=True).values_list("id", "valor")

def get_comuna(comuna_id):
    comuna = Comuna.objects.select_related("provincia__region").get(id=comuna_id)
    print("dentro del get_comuna", comuna)
    return {
        "provincia_id": comuna.provincia.id,
        "region_numero": comuna.provincia.region.numero
    }

def get_provincia(provincia_id):
    provincia = Provincia.objects.select_related("region").get(id=provincia_id)
    comunas = list(provincia.comunas.values("id", "nombre"))
    print("dentro del get_provincia", provincia, comunas)

    return {
        "region_numero": provincia.region.numero,
        "comunas": comunas
    }

def get_region(region_numero):
    region = Region.objects.get(numero=region_numero)
    provincias = list(region.provincias.values("id", "nombre"))
    comunas = list(Comuna.objects.filter(provincias__region=region).values("id","nombre"))
    print("dentro del get_region", region, provincias, comunas)
    return {
        "provincia_id": provincias,
        "comuna_id": comunas
    }
    
def get_content_permisos_detail(content_ids):
    modelos = []
    permisos = []


    content_types = ContentType.objects.filter(id__in=content_ids)
    DescripcionContent
    for content in content_types:
        desc_content, _ = DescripcionContent.objects.get_or_create(content=content)
        
        for permiso in content.permission_set.all():
            desc_permiso, _ = DescripcionPermiso.objects.get_or_create(permiso=permiso)
            permisos.append({
                "id": permiso.id,
                "content_id": desc_content.id,
                "app": desc_content.app,
                "modelo": desc_content.modelo,
                "codename": permiso.codename,
                "nombre": permiso.name,
                "descripcion": desc_permiso.descripcion,
                "date_created": desc_permiso.date_created,
            })
        
        modelos.append({
            "id": content.id,
            "app": desc_content.app,
            "modelo": desc_content.modelo,
            "descripcion": desc_content.descripcion,
            "bg_color": desc_content.bg_color,
            "icono": desc_content.icono,
            "url": reverse('permisos:modelos-detail', kwargs={'pk': content.id}),
            "date_created": desc_content.date_created
        })

    return {
        "modelos": modelos,
        "permisos": permisos,
    }


LIMITE_USUARIOS_PLAN = {
    "plan1": {"admin": 1, "user": 0},
    "plan2": {"admin": 1, "user": 2},
    "plan3": {"admin": 2, "user": 13},
}
# Helpers



def get_comuna(comuna_id):
    comuna = Comuna.objects.select_related("provincia__region").get(id=comuna_id)
    print("dentro del get_comuna", comuna)
    return {
        "provincia_id": comuna.provincia.id,
        "region_numero": comuna.provincia.region.numero
    }


def get_provincia(provincia_id):
    provincia = Provincia.objects.select_related("region").get(id=provincia_id)
    comunas = list(provincia.comunas.values("id", "nombre"))
    print("dentro del get_provincia", provincia, comunas)

    return {
        "region_numero": provincia.region.numero,
        "comunas": comunas
    }

def get_region(region_numero):
    region = Region.objects.get(numero=region_numero)
    provincias = list(region.provincias.values("id", "nombre"))
    comunas = list(Comuna.objects.filter(provincias__region=region).values("id","nombre"))
    print("dentro del get_region", region, provincias, comunas)
    return {
        "provincia_id": provincias,
        "comuna_id": comunas
    }
    