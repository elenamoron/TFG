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

    def get_queryset(self):
        logger_user = self.request.user
        return Organization.objects.filter(users=logger_user)

    def create(self, request, *args, **kwargs):

        data_document = {'name': request.data['name'], 'description': request.data['description'],
                         'nif': request.data['nif'], 'address': request.data['address'],
                         'created': request.data['created'], 'code': request.data['code']}

        organization = OrganizationSerializer(data=data_document)

        if organization.is_valid():
            new_organization = organization.save()
            new_organization.users.add(request.user)

            return Response(organization.data, status=status.HTTP_201_CREATED)
        else:
            Response({"Error"}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        organization = get_object_or_404(Organization, id=self.kwargs['pk'])
        serializer = OrganizationSerializer(organization, data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        response_serializer = OrganizationSerializer(organization)
        return Response(response_serializer.data, status.HTTP_202_ACCEPTED)

    def delete(self, request, *args, **kwargs):
        pass


class OrganizationMemberViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer

    def get_queryset(self):

        return Organization.objects.filter(id=self.kwargs['pk']).values('users')


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

    def get_queryset(self):
        return Project.objects.filter(organization=self.kwargs['pk'])


class ProjectsViewSet(viewsets.ModelViewSet):
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