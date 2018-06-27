from django.shortcuts import get_object_or_404
from rest_framework import status, views
from rest_framework import viewsets
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response

from client.models import LegalPerson, PhysicalPerson, Document
from client.serializers import LegalPersonSerializer, PhysicalPersonSerializer, FileSerializer, SupportSerializer
from organization.models import Project
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

    def get_queryset(self):
        return LegalPerson.objects.filter(project=self.kwargs['pk2'])

    def create(self, request, *args, **kwargs):
        data = {'denominacion_social': request.data['denominacion_social'], 'CIF': request.data['CIF'],
                'ubicacion': request.data['ubicacion'], 'fecha_constitucion': request.data['fecha_constitucion'],
                'sector': request.data['sector'], 'forma_juridica': request.data['forma_juridica'], 'registro':
                    request.data['registro'], 'numero_inscripciones': request.data['numero_inscripciones'], 'poblacion':
                    request.data['poblacion'], 'provincia': request.data['provincia'], 'codigo_postal':
                    request.data['codigo_postal'], 'pais': request.data['pais'], 'telefono': request.data['telefono'],
                'email': request.data['email']}

        legalPerson = LegalPersonSerializer(data=data)

        if legalPerson.is_valid():
            newLegalPerson = legalPerson.save()

            try:
                project = Project.objects.get(id=self.kwargs['pk2'], organization_id=self.kwargs['pk1'])
                newLegalPerson.project = project
                newLegalPerson.save()
                return Response(legalPerson.data, status=status.HTTP_201_CREATED)
            except ValueError:
                return Response({"Error no hay proyecto con ese Id"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            Response({"Error"}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        legalPerson = get_object_or_404(LegalPerson, project=self.kwargs['pk2'])
        serializer = LegalPersonSerializer(legalPerson, data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        response_serializer = LegalPersonSerializer(legalPerson)
        return Response(response_serializer.data, status.HTTP_202_ACCEPTED)


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

    def get_queryset(self):
        return PhysicalPerson.objects.filter(project=self.kwargs['pk2'])

    def create(self, request, *args, **kwargs):
        data = {'nombre_completo': request.data['nombre_completo'], 'documento_identificativo':
                request.data['documento_identificativo'], 'fecha_caducidad': request.data['fecha_caducidad'],
                'nacionalidad': request.data['nacionalidad'], 'pais_nacionalidad': request.data['pais_nacionalidad'],
                'lugar_nacimiento': request.data['lugar_nacimiento'], 'pais_residencia': request.data['pais_residencia']
                , 'domicilio': request.data['domicilio'], 'telefono': request.data['telefono'], 'email':
                    request.data['email'], 'capital': request.data['capital'], 'responsabilidad_publica':
                    request.data['responsabilidad_publica'], 'controla_sociedad': request.data['controla_sociedad'],
                'control': request.data['control'], 'relacion_negocios': request.data['relacion_negocios']}

        physicalPerson = PhysicalPersonSerializer(data=data)

        if physicalPerson.is_valid():
            newPhysicalPerson = physicalPerson.save()

            try:
                project = Project.objects.get(id=self.kwargs['pk2'], organization_id=self.kwargs['pk1'])
                newPhysicalPerson.project = project
                newPhysicalPerson.save()
                return Response(physicalPerson.data, status=status.HTTP_201_CREATED)
            except ValueError:
                return Response({"Error no hay proyecto con ese Id"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            Response({"Error"}, status=status.HTTP_400_BAD_REQUEST)


class SpecificPhysicalPersonViewSet(viewsets.ModelViewSet):
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

    def get_queryset(self):
        return PhysicalPerson.objects.filter(project=self.kwargs['pk2'], id=self.kwargs['id'])

    def update(self, request, *args, **kwargs):
        physicalperson = get_object_or_404(PhysicalPerson, project=self.kwargs['pk2'], id=self.kwargs['id'])
        serializer = PhysicalPersonSerializer(physicalperson, data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        response_serializer = PhysicalPersonSerializer(physicalperson)
        return Response(response_serializer.data, status.HTTP_202_ACCEPTED)

    def delete(self, request, *args, **kwargs):
        physicalperson = get_object_or_404(PhysicalPerson, project=self.kwargs['pk2'], id=self.kwargs['id'])
        physicalperson.delete()
        return Response({"PhysicalPerson delete"}, status.HTTP_200_OK)


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
