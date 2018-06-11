from django.contrib.auth.models import User
from django.db import models


class Organization(models.Model):
    created = models.DateField(blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, default='')
    description = models.CharField(max_length=255, blank=True, default='')
    code = models.TextField()
    address = models.CharField(max_length=255, blank=True, default='')
    nif = models.CharField(max_length=255, blank=True, default='')
    users = models.ManyToManyField(User, through='OrganizationUser',related_name='auditor')

    class Meta:
        ordering = ('created',)


class OrganizationUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)


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
    cliente = models.CharField(max_length=100, blank=True, default='')
    logo = models.CharField(max_length=255, blank=True, default='')
    activo = models.BooleanField(default=True)


class User(models.Model):
    email = models.CharField(max_length=255, blank=True, unique=True)
    password = models.CharField(max_length=255, blank=True)

