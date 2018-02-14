from rest_framework import serializers
from lpbc.models import Organization, Perfil

class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = ('id', 'name','description', 'code', 'cliente', 'logo')

class PerfilSerializer(serializers.ModelSerializer):
    class Meta:
        model = Perfil
        fields = ('id', 'user', 'nombre', 'apellidos', 'fecha_nacimiento', 'codigo_postal', 'telefono', 'mail', 'observaciones')