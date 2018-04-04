from django.db import models


# Create your models here.
class LegalPerson(models.Model):
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
    pais = models.CharField(max_length=10, blank=True)
    telefono = models.CharField(max_length=20, blank=True)
    email = models.CharField(max_length=255, blank=True)


class PhysicalPerson(models.Model):
    nombre_completo = models.CharField(max_length=255, blank=True)
    documento_identificativo = models.CharField(max_length=255, blank=True)
    fecha_caducidad = models.DateField(blank=True, null=True)
    nacionalidad = models.CharField(max_length=255, blank=True)
    pais_nacionalidad = models.CharField(max_length=255, blank=True)
    lugar_nacimiento = models.CharField(max_length=255, blank=True)
    pais_residencia = models.CharField(max_length=255, blank=True)
    domicilio = models.CharField(max_length=255, blank=True)
    telefono = models.CharField(max_length=20, blank=True)
    email = models.CharField(max_length=255, blank=True)
    acreditacion_poderes = models.BooleanField()


class Relationship(models.Model):
    relationship = models.CharField(max_length=255, blank=True)


class Document(models.Model):
    meta_descripcion = models.CharField(max_length=255, blank=True)
    blog = models.CharField(max_length=255, blank=True)


class RelationshipLegalPhysical(models.Model):
    persona_juridica = models.ForeignKey(LegalPerson, on_delete=models.CASCADE)
    persona_fisica = models.ForeignKey(PhysicalPerson, on_delete=models.CASCADE)
    tipo_relacion = models.ForeignKey(Relationship, on_delete=models.CASCADE)
    datos_particulares = models.CharField(max_length=255,blank=True)
    #documentos = models.ManyToOneRel(Documento)

