from django.contrib.auth.models import User
from django.db import models


class Organization(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()

    class Meta:
        ordering = ('created',)

class Perfil(models.Model):
    user = models.ForeignKey(User, null=True)
    nombre = models.CharField(max_length=100, blank=True)
    apellidos = models.CharField(max_length=255, blank=True)
    fecha_nacimiento = models.DateField(blank=True, null=True)
    codigo_postal = models.CharField(max_length=10,blank=True)
    telefono = models.CharField(max_length=20,blank=True)
    mail = models.CharField(max_length=255,blank=True)
    observaciones = models.TextField(blank=True)

    class Meta:
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfiles'

