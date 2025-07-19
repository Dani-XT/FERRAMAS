from django.apps import apps
from django.db.models.signals import post_migrate, post_save
from django.dispatch import receiver

from django.contrib.auth import get_user_model

# Modelos
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from apps.access.permisos.models import DescripcionPermiso, DescripcionContent
from auth.models import ProfileImage

User = get_user_model()
ProfileImage = apps.get_model('profile', 'ProfileImage')

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

@receiver(post_save, sender=User)
def crear_imagen_perfil(sender, instance, created, **kwargs):
    if created and not hasattr(instance, 'profileimage'):
        ProfileImage.objects.create(usuario=instance)