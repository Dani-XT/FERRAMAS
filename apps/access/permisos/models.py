from django.db import models
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.utils import timezone

# Create your models here.
class DescripcionPermiso(models.Model):
    # DescriptionPermission
    permiso = models.OneToOneField(Permission, on_delete=models.CASCADE, related_name="descripcion_permiso")
    descripcion = models.TextField(default="No existe una descripcion")
    bg_color = models.CharField(max_length=150, blank=True, null=True, default="")
    icono = models.CharField(max_length=150, blank=True, null=True, default="")
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "descripcion_permission"

    def __str__(self):
        return f"Metadatos de grupo: {self.group.name}"
    
class DescripcionContent(models.Model):
    content = models.OneToOneField(ContentType, on_delete=models.CASCADE, related_name="descripcion_content")
    app = models.CharField(max_length=100, blank=True, null=True)
    modelo = models.CharField(max_length=100, blank=True, null=True)
    descripcion = models.TextField(default="No existe una descripcion")
    bg_color = models.CharField(max_length=150, blank=True, null=True, default="")
    icono = models.CharField(max_length=150, blank=True, null=True, default="")
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "descripcion_content_type"

    def save(self, *args, **kwargs):
        if not self.app:
            self.app = self.content.app_label
        if not self.modelo:
            self.modelo = self.content.model
        
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Descripcion para {self.content.app_label}"