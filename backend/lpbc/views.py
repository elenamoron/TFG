from rest_framework import viewsets
from rest_framework.response import Response

from lpbc.models import Organization, Perfil
from lpbc.serializers import OrganizationSerializer, PerfilSerializer


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
