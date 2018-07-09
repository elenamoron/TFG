from django.shortcuts import get_object_or_404
from rest_framework import status, views
from rest_framework import viewsets
from rest_framework.response import Response
from django.contrib.auth.models import User
from organization.models import Organization, Profile, Project
from organization.serializers import OrganizationSerializer, ProfileSerializer, ProjectSerializer, UserSerializer

import json


class OrganizationViewSet(viewsets.ModelViewSet):

    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer

    def get_queryset(self):
        logger_user = self.request.user
        return Organization.objects.filter(users=logger_user)

    def retrieve(self, request, *args, **kwargs):
        logger_user = self.request.user
        organization = Organization.objects.get(id=self.kwargs['pk'], users=logger_user)
        return Response(OrganizationSerializer(organization).data, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):

        organization = OrganizationSerializer(data=request.data)

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
        organization = Organization.objects.get(id=self.kwargs['pk'])
        organization.delete()
        return Response({'Organization delete'}, status.HTTP_200_OK)


class OrganizationMemberViewSet(viewsets.ModelViewSet):
    serializer_class = OrganizationSerializer

    def get_queryset(self):

        return Organization.objects.filter(id=self.kwargs['pk'])

    def create(self, request, *args, **kwargs):
        organization = Organization.objects.get(id=self.kwargs['pk'])
        user = User.objects.get(id=self.kwargs['uuid'])
        organization.users.add(user)
        organization.save()
        return Response(UserSerializer(user).data, status.HTTP_200_OK)

    def delete(self):
        pass


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
        return Project.objects.filter(organization=self.kwargs['pk'],users=self.request.user)

    def create(self, request, *args, **kwargs):
        project = ProjectSerializer(data=request.data)

        if project.is_valid():
            new_project = project.save()
            organization = Organization.objects.get(id=self.kwargs['pk'])
            new_project.organization = organization
            new_project = project.save()

            new_project.users.add(request.user)

            return Response(project.data, status=status.HTTP_201_CREATED)
        else:
            Response({"Error"}, status=status.HTTP_400_BAD_REQUEST)


class ProjectsViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer

    def get_queryset(self):
        if self.kwargs['scope'] == 'active':
            return Project.objects.filter(organization=self.kwargs['pk'], activo=True, users=self.request.user)
        elif self.kwargs['scope'] == 'archive':
            return Project.objects.filter(organization=self.kwargs['pk'], activo=False, users=self.request.user)
        elif self.kwargs['scope'] == 'all':
            return Project.objects.filter(organization=self.kwargs['pk'])
        else:
            return Response({"Error no existe ninguna coincidencia con lo que solicita"}, status=status.HTTP_400_BAD_REQUEST)


class ProjectDetailView(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    def get_queryset(self):
        return Project.objects.filter(organization=self.kwargs['pk1'], id=self.kwargs['pk2'])

    def delete(self, request, *args, **kwargs):
        project = Project.objects.filter(organization=self.kwargs['pk1'], id=self.kwargs['pk2'])
        project.delete()
        return Response({"Project delete"}, status.HTTP_200_OK)

    def update(self, request, *args, **kwargs):
        project = get_object_or_404(Project, organization=self.kwargs['pk1'], id=self.kwargs['pk2'])
        serializer = ProjectSerializer(project, data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        response_serializer = ProjectSerializer(project)
        return Response(response_serializer.data, status.HTTP_202_ACCEPTED)
