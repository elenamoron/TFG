from rest_framework import serializers
from organization.models import Organization, Profile, Project, User


class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = ('id', 'name', 'description', 'code')


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('id', 'user', 'nombre', 'apellidos', 'fecha_nacimiento', 'codigo_postal', 'telefono', 'mail',
                  'observaciones')


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('id', 'name', 'description', 'fecha_creacion', 'cliente', 'logo', 'activo')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'password')
