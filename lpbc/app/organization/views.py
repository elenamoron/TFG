from django.shortcuts import get_object_or_404
from rest_framework import status, views
from rest_framework import viewsets
from rest_framework.response import Response

from organization.models import Organization, Profile, Project, User
from organization.serializers import OrganizationSerializer, ProfileSerializer, ProjectSerializer, UserSerializer

import json


class OrganizationViewSet(viewsets.ModelViewSet):

    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer

    def create(self, request, *args, **kwargs):
        logged_user = request.user

        data_document = {'name': request.data['name'], 'description': request.data['description'],
                         'nif': request.data['nif'], 'address': request.data['address'],
                         'created': request.data['created'], 'code': request.data['code'],
                         'users': logged_user}

        organization = OrganizationSerializer(data=data_document)
        import ipdb
        ipdb.set_trace()

        if organization.is_valid():
            organization.save()
            #logged_user = request.user
            #organization.users.add(logged_user)


            return Response({"Organization created"}, status=status.HTTP_201_CREATED)
        else:
            Response({"Error"}, status=status.HTTP_400_BAD_REQUEST)


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


class ProjectViewSet(viewsets.ModelViewSet):
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
    serializer_class = ProjectSerializer


class ProjectActive(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer

    def get_queryset(self):
        return Project.objects.filter(activo=True)


class ProjectArchive(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer

    def get_queryset(self):
        return Project.objects.filter(activo=False)


class ProjectByName(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer

    def get_queryset(self):

        name = self.kwargs['name']
        return Project.objects.filter(name=name)


class ProjectDetailView(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer