from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response

from lpbc.models import Organization, Perfil, Proyecto
from lpbc.serializers import OrganizationSerializer, PerfilSerializer, ProyectoSerializer


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

class PerfilViewSet(viewsets.ModelViewSet):
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
    queryset = Perfil.objects.all()
    serializer_class = PerfilSerializer

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
    queryset = Proyecto.objects.all()
    serializer_class = ProyectoSerializer

class ProyectoActive(viewsets.ModelViewSet):
    serializer_class = ProyectoSerializer

    def get_queryset(self):

        activo = self.kwargs['activo']
        return Proyecto.objects.filter(proyecto__activo=activo)

class ProyectoByName(viewsets.ModelViewSet):
    serializer_class = ProyectoSerializer

    def get_queryset(self):

        name = self.kwargs['name']
        return Proyecto.objects.filter(proyecto__name=name)