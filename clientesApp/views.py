from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions, AllowAny
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
import datetime
from rest_framework.decorators import action



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

    @action(detail=True, methods=['post'])
    def atribui_endereco(self, request, pk=None):
        endereco = self.request.query_params.get('id_endereco', None)
        
        if endereco:
            try:
                endereco = Enderecos.objects.get(id_endereco=endereco)
                cliente = Clientes.objects.get(id_cliente=int(pk))
                endereco.id_cliente = cliente
                endereco.save()

                return Response({'message':'Endereço atribuido ao cliente '+endereco.id_cliente.nome+' com sucesso!!'})
            except:
                return Response({'message':'Endereço ou cliente não encontrado'}, status=404)

        return Response({'message':'adicione o atributo id_endereco na query_params'}, status=401)

    @action(detail=True, methods=['post'])
    def atribui_endereco_principal(self, request, pk=None):
        endereco = self.request.query_params.get('id_endereco', None)
        
        if endereco:
            try:
                #Ler o endereço que vem na query_params
                endereco = Enderecos.objects.get(id_endereco=endereco)

                #ler o cliente que vem na url
                cliente = Clientes.objects.get(id_cliente=int(pk))

                #remove atualiza o campo principal para false, caso exista alguma instancia
                Enderecos.objects.filter(id_cliente=cliente, prncipal=True).update(principal=False)
                endereco.id_cliente = cliente
                endereco.principal = True
                endereco.save()

                return Response({'message':'Endereço principal atribuido ao cliente '+cliente.nome+' com sucesso!!'})
            except:
                return Response({'message':'Endereço ou cliente não encontrado'}, status=404)

        return Response({'message':'adicione o atributo id_endereco na query_params'}, status=401)


class EnderecoViewSet(viewsets.ModelViewSet):
    queryset = Enderecos.objects.all()
    serializer_class = EnderecoSerializer
    authentication_classes = (
        JSONWebTokenAuthentication, SessionAuthentication)
    permission_classes = [DjangoModelPermissions]
