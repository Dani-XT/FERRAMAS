from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class ProfileImage(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name="avatar")
    imagen = models.ImageField(upload_to="usuarios/profile/", default="usuarios/profile/otro.png")