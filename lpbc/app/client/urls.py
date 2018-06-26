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
from client.views import LegalPersonViewSet, PhysicalPersonViewSet, LegalPersonFromProjectViewSet, \
    PhysicalPersonFromProjectViewSet, PhysicalPersonByIdViewSet, DocumentUploadView, PhysicalPersonWithCapitalViewSet

urlpatterns = [
    path('<int:pk1>/project/<int:pk2>/LegalPerson/', LegalPersonViewSet.as_view({'get': 'list', 'post': 'create',
                                                                                 'put': 'update'})),
    path('<int:pk1>/project/<int:pk2>/PhysicalPerson/', PhysicalPersonViewSet.as_view({'get': 'list',
                                                                                       'post': 'create'})),
    path('<int:pk1>/project/<int:pk2>/PhysicalPerson/<int:id>', PhysicalPersonFromProjectViewSet.as_view({'get': 'list',
                                                                                                          'put':
                                                                                                              'update',
                                                                                                          'delete':
                                                                                                              'delete'}
                                                                                                         )),
    path('document/', DocumentUploadView.as_view())
]


