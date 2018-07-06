from django.db import models
from organization.models import Project
from django.core.files.storage import FileSystemStorage

# Create your models here.


class LegalPerson(models.Model):
    project = models.ForeignKey(Project, null=True, on_delete=models.CASCADE)
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
    project = models.ForeignKey(Project, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, blank=True)
    identificationDocument = models.CharField(max_length=255, blank=True)
    deliveryDate = models.DateField(blank=True, null=True)
    nacionality = models.CharField(max_length=255, blank=True)
    nacionalityCountry = models.CharField(max_length=255, blank=True)
    birthplace = models.CharField(max_length=255, blank=True)
    country = models.CharField(max_length=255, blank=True)
    address = models.CharField(max_length=255, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    email = models.CharField(max_length=255, blank=True)
    hasCapital = models.BooleanField(default=False)
    hasPublicResponsability = models.BooleanField(default=False)
    hasSocietyControl = models.BooleanField(default=False)
    hasControl = models.BooleanField(default=False)
    hasBussinesRelation = models.BooleanField(default=False)
    isPublicResponsabilityOtherCountry = models.BooleanField(default=False)
    publicResponsabilityCountries = models.CharField(max_length=255, blank=True, null=True)
    relationPublicResponsability = models.CharField(max_length=255, blank=True, null=True)
    typeSocietyControl = models.CharField(max_length=255, blank=True, null=True)
    typeControl = models.CharField(max_length=255, blank=True, null=True)
    typeBussinesRelation = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        ordering = ('name',)


class Relationship(models.Model):
    relationship = models.CharField(max_length=255, blank=True)


'''fs = FileSystemStorage(location='/media/photos')'''


class Document(models.Model):
    content_type = models.CharField(max_length=255, blank=True)
    length = models.CharField(max_length=255, blank=True)
    file = models.FileField(blank=True, null=True)


class RelationshipLegalPhysical(models.Model):
    persona_juridica = models.ForeignKey(LegalPerson, on_delete=models.CASCADE)
    persona_fisica = models.ForeignKey(PhysicalPerson, on_delete=models.CASCADE)
    tipo_relacion = models.ForeignKey(Relationship, on_delete=models.CASCADE)
    datos_particulares = models.CharField(max_length=255, blank=True)
    #documentos = models.ManyToOneRel(Documento)


class SupportDoc(models.Model):
    cod_justificacion = models.CharField(max_length=255, blank=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True)
    persona_juridica = models.ForeignKey(LegalPerson, null=True, blank=True, on_delete=models.CASCADE)
    persona_fisica = models.ForeignKey(PhysicalPerson, null=True, blank=True, on_delete=models.CASCADE)