from rest_framework import serializers
from organization.models import Organization, Profile, Proyecto

class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = ('id', 'name','description', 'code')

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('id', 'user', 'nombre', 'apellidos', 'fecha_nacimiento', 'codigo_postal', 'telefono', 'mail', 'observaciones')

class ProyectoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proyecto
        fields = ('id', 'name','description', 'fecha_creacion', 'cliente', 'logo','activo')