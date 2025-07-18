from django.db import models


class GrupoValor(models.Model):
    nombre = models.CharField(max_length=150, unique=True)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre

class ValorSistema(models.Model):
    grupo = models.ForeignKey(GrupoValor, on_delete=models.CASCADE, related_name="valor_sistema")
    
    is_plural = models.BooleanField(default=True)
    clave = models.CharField(max_length=100, unique=True)
    valor = models.CharField(max_length=255)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.clave}: {self.valor}"
    
    
class Region(models.Model):
    numero = models.IntegerField()
    nombre = models.CharField(max_length=150)

    def __str__(self):
        return self.nombre

class Provincia(models.Model):
    nombre = models.CharField(max_length=150)
    nombre_completo = models.CharField(max_length=200)
    region = models.ForeignKey(Region, on_delete=models.CASCADE, related_name="provincias")

    def __str__(self):
        return self.nombre

class Comuna(models.Model):
    nombre = models.CharField(max_length=150)
    provincia = models.ForeignKey(Provincia, on_delete=models.CASCADE, related_name="comunas")

    def __str__(self):
        return self.nombre