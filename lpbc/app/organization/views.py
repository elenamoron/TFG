from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response

from organization.models import Organization, Profile, Project
from organization.serializers import OrganizationSerializer, ProfileSerializer, ProyectoSerializer


class OrganizationViewSet(viewsets.ModelViewSet):
    """
        retrieve:
            Return a organization instance.

        list:
            Return all organizations, ordered by most recently joined.

        create:
            Create a new organization.

        delete:
            Remove an existing organization.

        partial_update:
            Update one or more fields on an existing organization.

        update:
            Update a organization.
        """
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer

class ProfileViewSet(viewsets.ModelViewSet):
    """
        retrieve:
            Return a perfil instance.

        list:
            Return all perfiles, ordered by most recently joined.

        create:
            Create a new perfil.

        delete:
            Remove an existing perfil.

        partial_update:
            Update one or more fields on an existing perfil.

        update:
            Update a perfil.
        """
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class ProyectoViewSet(viewsets.ModelViewSet):
    """
        retrieve:
            Return a proyecto instance.

        list:
            Return all ptroyectos, ordered by most recently joined.

        create:
            Create a new proyecto.

        delete:
            Remove an existing proyecto.

        partial_update:
            Update one or more fields on an existing proyecto.

        update:
            Update a proyecto.
        """
    queryset = Project.objects.all()
    serializer_class = ProyectoSerializer

class ProyectoActive(viewsets.ModelViewSet):
    serializer_class = ProyectoSerializer

    def get_queryset(self):
        return Project.objects.filter(proyecto__activo=True)

class ProyectoByName(viewsets.ModelViewSet):
    serializer_class = ProyectoSerializer

    def get_queryset(self):

        name = self.kwargs['name']
        return Project.objects.filter(proyecto__name=name)