from django.contrib import admin
from .models import Profile, Organization, Project
# Register your models here.

class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('created','name', 'code')


admin.site.register(Organization, OrganizationAdmin)

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'nombre', 'apellidos', 'telefono', 'mail', 'codigo_postal', 'observaciones')
    search_fields = ('user__username','nombre','apellidos')

admin.site.register(Profile, ProfileAdmin)

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'fecha_creacion')

admin.site.register(Project, ProjectAdmin)

