from django.contrib.auth.models import User
from django.db import models


class Organization(models.Model):
    created = models.DateField(blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, default='', unique=True)
    description = models.CharField(max_length=255, blank=True, default='')
    code = models.CharField(max_length=100, unique=True, default='')
    address = models.CharField(max_length=255, blank=True, default='')
    nif = models.CharField(max_length=255, blank=True, default='', unique=True)
    users = models.ManyToManyField(User)

    class Meta:
        ordering = ('created',)


class Profile(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100, blank=True)
    apellidos = models.CharField(max_length=255, blank=True)
    fecha_nacimiento = models.DateField(blank=True, null=True)
    codigo_postal = models.CharField(max_length=10, blank=True)
    telefono = models.CharField(max_length=20, blank=True)
    mail = models.CharField(max_length=255, blank=True)
    observaciones = models.TextField(blank=True)

    class Meta:
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfiles'


class Project(models.Model):
    name = models.CharField(max_length=100, blank=True, default='')
    description = models.CharField(max_length=255, blank=True, default='')
    fecha_creacion = models.DateField(blank=True, null=True)
    cliente = models.CharField(max_length=100, blank=True, default='', null=True)
    logo = models.CharField(max_length=255, blank=True, default='')
    activo = models.BooleanField(default=True)
    organization = models.ForeignKey(Organization, null=True, on_delete=models.CASCADE)
    users = models.ManyToManyField(User)


