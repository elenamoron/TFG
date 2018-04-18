from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response

from client.models import LegalPerson
from client.serializers import LegalPersonSerializer


class LegalPersonViewSet(viewsets.ModelViewSet):
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
    queryset = LegalPerson.objects.all()
    serializer_class = LegalPersonSerializer