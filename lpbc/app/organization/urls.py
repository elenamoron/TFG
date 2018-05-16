"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.urls import path
from django.urls import re_path
from rest_framework import routers
from django.conf.urls import url
from organization.views import OrganizationViewSet, ProfileViewSet, ProjectActive, ProjectViewSet, ProjectByName, \
    DocumentUploadView, ProjectDetailView, ProjectArchive


urlpatterns = [
    path('organization', OrganizationViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('profile', ProfileViewSet),
    path('project/', ProjectViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('project/<int:pk>/', ProjectDetailView.as_view({'put': 'update'})),
    path('project/active', ProjectActive.as_view({'get': 'list'})),
    path('project/archive', ProjectArchive.as_view({'get': 'list'})),
    path('project/<str:name>/', ProjectByName.as_view({'get': 'list'})),
    path('document/<str:filename>', DocumentUploadView.as_view())
]


