from django.shortcuts import render
from rest_framework import viewsets, mixins
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

    #método para inserir o campo id_user_cad e registrar o usuário que cadastrou a instância
    def perform_create(self, serializer):
        serializer.save(id_user_cad=self.request.user)

    #método para inserir o campo id_user_alt e registrar o usuário que alterou a instância
    def perform_update(self, serializer):
        serializer.save(id_user_alt=self.request.user)

   
class EnderecoViewSet(viewsets.ModelViewSet):
    queryset = Enderecos.objects.all()
    serializer_class = EnderecoSerializer
    authentication_classes = (
        JSONWebTokenAuthentication, SessionAuthentication)
    permission_classes = [DjangoModelPermissions]

    #método para inserir o campo id_user_cad e registrar o usuário que cadastrou a instância
    def perform_create(self, serializer):
        serializer.save(id_user_cad=self.request.user)

    #método para inserir o campo id_user_alt e registrar o usuário que alterou a instância
    def perform_update(self, serializer):
        serializer.save(id_user_alt=self.request.user)



class AtribuiViewSet(viewsets.GenericViewSet):
    queryset = Clientes.objects.all()
    serializer_class = AtribuiSerializer
    authentication_classes = (
        JSONWebTokenAuthentication, SessionAuthentication)
    permission_classes = [DjangoModelPermissions]

    @action(detail=False, methods=['post'])
    def demais(self, request):
        """\nEndpoint para vincular Endereço a um Cliente\n"""
        serializer = UserSerializer
        endereco = self.request.query_params.get('id_endereco', None)
        
      
        try:
            #Ler o endereço que vem no body
            endereco = Enderecos.objects.get(id_endereco=int(request.data['id_endereco']))

            #ler o cliente que vem no body
            cliente = Clientes.objects.get(id_cliente=int(request.data['id_cliente']))

            #vincula o cliente ao endereço
            endereco.id_cliente = cliente

            #altera o campo principal, para evitar que o banco fique inconsistente
            endereco.principal = False

            #registra o usuário que atualizou a instância
            endereco.id_user_cad = request.user
            endereco.save()

            return Response({'message':'Endereço atribuido ao cliente '+endereco.id_cliente.nome+' com sucesso!!'})

        except:
            return Response({'message':'Endereço ou cliente não encontrado'}, status=404)


    @action(detail=False, methods=['post'])
    def principal(self, request):
        """Endpoint para vincular Endereço Principal a um Cliente"""
        
        
        try:
            #Ler o endereço que vem no body
            endereco = Enderecos.objects.get(id_endereco=int(request.data['id_endereco']))

            #ler o cliente que vem no body
            cliente = Clientes.objects.get(id_cliente=int(request.data['id_cliente']))

            # atualiza o campo principal para false, caso exista alguma instancia
            Enderecos.objects.filter(id_cliente=cliente, prncipal=True).update(principal=False)

            #vincula o endereço ao cliente
            endereco.id_cliente = cliente

            #define o endereço como principal
            endereco.principal = True

            endereco.id_user_cad = request.user
            endereco.save()

            return Response({'message':'Endereço principal atribuido ao cliente '+cliente.nome+' com sucesso!!'})
        except:
            return Response({'message':'Endereço ou cliente não encontrado'}, status=404)

    
