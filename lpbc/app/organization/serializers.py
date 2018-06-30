from rest_framework import serializers
from organization.models import Organization, Profile, Project
from django.contrib.auth.models import User as DjangoUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = DjangoUser
        fields = ("username", "email")


class OrganizationSerializer(serializers.ModelSerializer):
    users = UserSerializer(many=True, read_only=True)

    class Meta:
        model = Organization
        fields = ('id', 'name', 'description', 'code', 'created', 'address', 'nif', 'users')


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('id', 'user', 'nombre', 'apellidos', 'fecha_nacimiento', 'codigo_postal', 'telefono', 'mail',
                  'observaciones')


class ProjectSerializer(serializers.ModelSerializer):
    users = UserSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = ('id', 'name', 'description', 'fecha_creacion', 'cliente', 'logo', 'activo', 'organization_id', 'users')


