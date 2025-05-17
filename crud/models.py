from django.db import models

class CRUDEntry(models.Model):
    class Meta:
        verbose_name = "Acceso a CRUD"
        verbose_name_plural = "Accesos a CRUD"

    def __str__(self):
        return "Acceso a CRUD"