from django.db import models
from django.contrib.auth.models import Group, Permission


from django.core.exceptions import ValidationError

# Create your models here.
class DescripcionGrupo(models.Model):
    grupo = models.OneToOneField(Group, on_delete=models.CASCADE, related_name="descripcion")
    descripcion = models.TextField(default="Sin descripcion")
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.grupo.name}"
