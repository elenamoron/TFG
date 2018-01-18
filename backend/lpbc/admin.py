from django.contrib import admin
from .models import Perfil, Organization, Proyecto, PersonaFisica, PersonaJuridica, Relacion, Documento, RelacionJuridicaFisica
# Register your models here.

class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('created','name', 'code')


admin.site.register(Organization, OrganizationAdmin)

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'nombre', 'apellidos', 'telefono', 'mail', 'codigo_postal', 'observaciones')
    search_fields = ('user__username','nombre','apellidos')

admin.site.register(Perfil, ProfileAdmin)

class ProyectoAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'fecha_creacion')

admin.site.register(Proyecto, ProyectoAdmin)

class PersonaJuridicaAdmin(admin.ModelAdmin):
    list_display = ('denominacion_social', 'CIF', 'ubicacion', 'fecha_constitucion', 'sector', 'forma_juridica', 'registro',
        'numero_inscripciones', 'poblacion', 'provincia', 'codigo_postal', 'pais', 'telefono', 'email')

admin.site.register(PersonaJuridica,PersonaJuridicaAdmin)

class PersonaFisicaAdmin(admin.ModelAdmin):
    list_display = ('nombre_completo', 'documento_identificativo', 'fecha_caducidad', 'nacionalidad', 'pais_nacionalidad',
        'lugar_nacimiento', 'pais_residencia', 'domicilio', 'telefono', 'email', 'acreditacion_poderes')

admin.site.register(PersonaFisica,PersonaFisicaAdmin)

class RelacionAdmin(admin.ModelAdmin):
    list_display = ('relacion')

admin.site.register(Relacion, RelacionAdmin)

class DocumentoAdmin(admin.ModelAdmin):
    list_display('meta_descripcion', 'blog')

admin.site.register(Documento, DocumentoAdmin)

class RelacionJuridicaFisicaAdmin(admin.ModelAdmin):
    list_display('persona_juridica', 'persona_fisica', 'tipo_relacion', 'datos_particulares')
    #documentos = models.ManyToOneRel(Documento)

admin.site.register(RelacionJuridicaFisica, RelacionJuridicaFisicaAdmin)

