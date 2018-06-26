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
    ProjectDetailView, ProjectArchive, ProjectsViewSet


urlpatterns = [
    path('', OrganizationViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('<int:pk>', OrganizationViewSet.as_view({'put': 'update', 'delete': 'delete'})),
    path('<int:pk>/member/<int:uuid>', OrganizationViewSet.as_view({'post': 'create', 'delete': 'delete'})),
    path('<int:pk>/member/', OrganizationViewSet.as_view({'get': 'list'})),
    path('profile/', ProfileViewSet.as_view({'post': 'create'})),
    path('profile/<int:pk>', ProfileViewSet.as_view({'get': 'list', 'put': 'update'})),
    path('<int:pk>/project/', ProjectViewSet.as_view({'post': 'create'})),
    path('<int:pk>/project/<str:scope>', ProjectsViewSet.as_view({'get': 'list'})),
    path('<int:pk1>/project/<int:pk2>/', ProjectDetailView.as_view({'get': 'list', 'put': 'update', 'delete': 'delete'})),
]


