from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response

from client.models import LegalPerson, PhysicalPerson
from client.serializers import LegalPersonSerializer, PhysicalPersonSerializer
from organization.models import Project


class LegalPersonViewSet(viewsets.ModelViewSet):
    """
        retrieve:
            Return a LegalPerson instance.

        list:
            Return all LegalPersons, ordered by most recently joined.

        create:
            Create a new LegalPerson.
            parameters:
            - name: id_project
              type: int

        delete:
            Remove an existing LegalPerson.

        partial_update:
            Update one or more fields on an existing LegalPerson.

        update:
            Update a LegalPerson.
        """
    queryset = LegalPerson.objects.all()
    serializer_class = LegalPersonSerializer


class LegalPersonFromProjectViewSet(viewsets.ModelViewSet):
    """
            retrieve:
                Return a LegalPerson instance.

            list:
                Return all LegalPersons, ordered by most recently joined.

            create:
                Create a new LegalPerson.
                parameters:
                - name: id_project
                  type: int

            delete:
                Remove an existing LegalPerson.

            partial_update:
                Update one or more fields on an existing LegalPerson.

            update:
                Update a LegalPerson.
            """

    serializer_class = LegalPersonSerializer

    def get_queryset(self):
        id_project = self.kwargs['idProject']
        return LegalPerson.objects.filter(project=id_project)

    def update(self, request, *args, **kwargs):
        legal_person = get_object_or_404(LegalPerson, project_id=kwargs['idProject'])
        serializer = LegalPersonSerializer(legal_person, data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        response_serializer = LegalPersonSerializer(legal_person)
        return Response(response_serializer.data, status.HTTP_202_ACCEPTED)


class PhysicalPersonViewSet(viewsets.ModelViewSet):
    """
        retrieve:
            Return a PhysicalPerson instance.

        list:
            Return all PhysicalPersons, ordered by most recently joined.

        create:
            Create a new PhysicalPerson.
            parameters:
            - name: id_project
              type: int

        delete:
            Remove an existing PhysicalPerson.

        partial_update:
            Update one or more fields on an existing PhysicalPerson.

        update:
            Update a LegalPerson.
        """
    queryset = PhysicalPerson.objects.all()
    serializer_class = PhysicalPersonSerializer


class PhysicalPersonFromProjectViewSet(viewsets.ModelViewSet):
    """
            retrieve:
                Return a PhysicalPerson instance.

            list:
                Return all PhysicalPersons, ordered by most recently joined.

            create:
                Create a new PhysicalPerson.
                parameters:
                - name: id_project
                  type: int

            delete:
                Remove an existing PhysicalPerson.

            partial_update:
                Update one or more fields on an existing PhysicalPerson.

            update:
                Update a LegalPerson.
            """

    serializer_class = PhysicalPersonSerializer

    def get_queryset(self):
        id_project = self.kwargs['idProject']
        return PhysicalPerson.objects.filter(project=id_project)

    def update(self, request, *args, **kwargs):
        physical_person = get_object_or_404(PhysicalPerson, project_id=kwargs['idProject'])
        serializer = PhysicalPersonSerializer(physical_person, data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        response_serializer = PhysicalPersonSerializer(physical_person)
        return Response(response_serializer.data, status.HTTP_202_ACCEPTED)

