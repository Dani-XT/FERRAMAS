from django.db.models.signals import post_migrate
from django.dispatch import receiver

# Modelos
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from apps.access.permisos.models import DescripcionPermiso, DescripcionContent

@receiver(post_migrate)
def crear_descripcion_automatica(sender, app_config, **kwargs):
    # Crear descripciones para ContentType
    for content in ContentType.objects.filter(app_label=app_config.label):
        DescripcionContent.objects.get_or_create(content=content)

    for permiso in Permission.objects.filter(content_type__app_label=app_config.label):
        # Si el nombre aún tiene formato original ("Can add logentry")
        if permiso.name.lower().startswith("can add") or \
           permiso.name.lower().startswith("can change") or \
           permiso.name.lower().startswith("can delete") or \
           permiso.name.lower().startswith("can view"):

            descripcion = permiso.name


            accion = permiso.codename.split("_")[0].capitalize()
            permiso.name = accion
            permiso.save()

            DescripcionPermiso.objects.update_or_create(
                permiso=permiso,
                defaults={"descripcion": descripcion}
            )