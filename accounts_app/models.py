from django.db import models
from django.conf import settings

from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    is_registrar = models.BooleanField(default=False)
    is_hod = models.BooleanField(default=False)


class Registrar(models.Model):
    registrar = models.OneToOneField(
        settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.CASCADE)
    about = models.TextField(null=True)

    def __str__(self):
        return self.registrar.username
