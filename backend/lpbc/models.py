from django.contrib.auth.models import User
from django.db import models


class Organization(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, blank=True, default='')
    description = models.CharField(max_length=255, blank=True, default='')
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

class Proyecto(models.Model):
    name = models.CharField(max_length=100, blank=True, default='')
    description = models.CharField(max_length=255, blank=True, default='')
    fecha_creacion = models.DateField(blank=True, null=True)
    cliente = models.CharField(max_length=100, blank=True, default='')
    logo = models.CharField(max_length=255, blank=True, default='')
    activo = models.BooleanField(default=True)

class PersonaJuridica(models.Model):
    denominacion_social = models.CharField(max_length=100, blank=True, default='')
    CIF = models.CharField(max_length=100, blank=True, default='')
    ubicacion = models.CharField(max_length=100, blank=True, default='')
    fecha_constitucion = models.DateField(blank=True, null=True)
    sector = models.CharField(max_length=100, blank=True, default='')
    forma_juridica = models.CharField(max_length=100, blank=True, default='')
    registro = models.CharField(max_length=100, blank=True, default='')
    numero_inscripciones = models.IntegerField()
    poblacion = models.CharField(max_length=100, blank=True, default='')
    provincia = models.CharField(max_length=100, blank=True, default='')
    codigo_postal = models.CharField(max_length=10, blank=True)
    pais = models.CharField(max_length=10,blank=True)
    telefono = models.CharField(max_length=20,blank=True)
    email = models.CharField(max_length=255,blank=True)

class PersonaFisica(models.Model):
    nombre_completo = models.CharField(max_length=255,blank=True)
    documento_identificativo = models.CharField(max_length=255,blank=True)
    fecha_caducidad = models.DateField(blank=True, null=True)
    nacionalidad = models.CharField(max_length=255,blank=True)
    pais_nacionalidad = models.CharField(max_length=255,blank=True)
    lugar_nacimiento = models.CharField(max_length=255,blank=True)
    pais_residencia = models.CharField(max_length=255,blank=True)
    domicilio = models.CharField(max_length=255,blank=True)
    telefono = models.CharField(max_length=20,blank=True)
    email = models.CharField(max_length=255, blank=True)
    acreditacion_poderes = models.BooleanField()

class Relacion(models.Model):
    relacion = models.CharField(max_length=255,blank=True)

class Documento(models.Model):
    meta_descripcion = models.CharField(max_length=255,blank=True)
    blog = models.CharField(max_length=255,blank=True)

class RelacionJuridicaFisica(models.Model):
    persona_juridica = models.ForeignKey(PersonaJuridica, on_delete=models.CASCADE)
    persona_fisica = models.ForeignKey(PersonaFisica, on_delete=models.CASCADE)
    tipo_relacion = models.ForeignKey(Relacion, on_delete=models.CASCADE)
    datos_particulares = models.CharField(max_length=255,blank=True)
    #documentos = models.ManyToOneRel(Documento)

