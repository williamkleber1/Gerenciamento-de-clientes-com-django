from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions, AllowAny
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
import datetime


from .serializers import *


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = (
        JSONWebTokenAuthentication, SessionAuthentication)
    permission_classes = [DjangoModelPermissions]


class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Clientes.objects.all()
    serializer_class = ClienteSerializer
    authentication_classes = (
        JSONWebTokenAuthentication, SessionAuthentication)
    permission_classes = [DjangoModelPermissions]


class EnderecoViewSet(viewsets.ModelViewSet):
    queryset = Enderecos.objects.all()
    serializer_class = EnderecoSerializer
    authentication_classes = (
        JSONWebTokenAuthentication, SessionAuthentication)
    permission_classes = [DjangoModelPermissions]