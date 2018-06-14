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

    def post(self, request, *args, **kwargs):
        data_document = {'name': request.data['name'], 'description': request.data['description'],
                         'nif': request.data['nif'], 'address': request.data['address'],
                         'created': request.data['created'], 'code': request.data['code']}
        organization = OrganizationSerializer(data=data_document)
        if organization.is_valid():
            organization.save()
            '''email = request.data['users[0][email]']

            user = User.objects.get_or_create(email=email)
            OrganizationUser.objects.create(user=user, organization=organization)'''
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


class RegisterView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class LoginView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def post(self,request, *args, **kwargs):
        import ipdb
        ipdb.set_trace()
        email = kwargs['email']
        user = User.objects.filter(email=email)
        if(user):
            if(user.password == kwargs['password']):
                return Response({"User": "login"}, status=status.HTTP_200_OK)
            else:
                return Response({"Error": "Contraseña incorrecta"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"Error": "No exite usuario con ese email"}, status=status.HTTP_400_BAD_REQUEST)

