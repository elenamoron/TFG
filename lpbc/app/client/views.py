from django.shortcuts import get_object_or_404
from rest_framework import status, views
from rest_framework import viewsets
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response

from client.models import LegalPerson, PhysicalPerson, Document
from client.serializers import LegalPersonSerializer, PhysicalPersonSerializer, FileSerializer, SupportSerializer

import json


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


class PhysicalPersonByIdViewSet(viewsets.ModelViewSet):
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
    queryset = PhysicalPerson.objects.all()


class DocumentUploadView(views.APIView):
    parser_classes = (MultiPartParser, FormParser)

    queryset = Document.objects.all()

    def get(self, *args, **kwargs):
        qs = super(DocumentUploadView, self).get_queryset(*args, **kwargs)
        qs = qs.filter(id=1)
        return qs

    def post(self, request, *args, **kwargs):
        for file in request.FILES:
            data = json.loads(request.data['json'])
            data_document = {}
            data_document['file'] = request.FILES[file]
            data_document['content_type'] = data['content_type']
            data_document['length'] = data['length']
            data_support = {}
            data_support['project'] = data['project']
            if data.get('persona_juridica'):
                data_support['persona_juridica'] = data['persona_juridica']
            if data.get('persona_fisica'):
                data_support['persona_fisica'] = data['persona_fisica']
            data_support['cod_justificacion'] = data['tag']
            file_serializer = FileSerializer(data=data_document)
            support_serializer = SupportSerializer(data=data_support)
            if file_serializer.is_valid() and support_serializer.is_valid():
                file_serializer.save()
                support_serializer.save()
                return Response(file_serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class PhysicalPersonWithCapitalViewSet(viewsets.ModelViewSet):
    serializer_class = PhysicalPersonSerializer

    def get_queryset(self):
        id_project = self.kwargs['idProject']
        return PhysicalPerson.objects.filter(project=id_project, capital=True)
