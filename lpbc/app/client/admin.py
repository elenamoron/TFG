from django.contrib import admin

# Register your models here.
from client.models import LegalPerson, PhysicalPerson, Relationship, Document, RelationshipLegalPhysical


class LegalPersonAdmin(admin.ModelAdmin):
    list_display = ('denominacion_social', 'CIF', 'ubicacion', 'fecha_constitucion', 'sector', 'forma_juridica',
                    'registro', 'numero_inscripciones', 'poblacion', 'provincia', 'codigo_postal', 'pais', 'telefono',
                    'email')

admin.site.register(LegalPerson, LegalPersonAdmin)


class RelationshipAdmin(admin.ModelAdmin):
    list_display = ('relationship',)

admin.site.register(Relationship, RelationshipAdmin)


class RelationshipLegalPhysicalAdmin(admin.ModelAdmin):
    list_display = ('persona_juridica', 'persona_fisica', 'tipo_relacion', 'datos_particulares')
    # documentos = models.ManyToOneRel(Documento)

admin.site.register(RelationshipLegalPhysical, RelationshipLegalPhysicalAdmin)

