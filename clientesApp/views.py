from django.shortcuts import render
from rest_framework import viewsets, mixins
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions, AllowAny
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
import datetime
from rest_framework.decorators import action
from .helper import *



from .serializers import *
from .paginations import CustomPagination


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = CustomPagination
    authentication_classes = (
        JSONWebTokenAuthentication, SessionAuthentication)
    permission_classes = [DjangoModelPermissions]


class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Clientes.objects.all()
    serializer_class = ClienteSerializer
    pagination_class = CustomPagination
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
    pagination_class = CustomPagination
    authentication_classes = (
        JSONWebTokenAuthentication, SessionAuthentication)
    permission_classes = [DjangoModelPermissions]

    #método para inserir o campo id_user_cad e registrar o usuário que cadastrou a instância
    def perform_create(self, serializer):
        serializer.save(id_user_cad=self.request.user)

    #método para inserir o campo id_user_alt e registrar o usuário que alterou a instância
    def perform_update(self, serializer):
        serializer.save(id_user_alt=self.request.user)


#View para vincular o cliente a um endereço
class AtribuiViewSet(viewsets.GenericViewSet):
    queryset = Clientes.objects.all()
    serializer_class = AtribuiSerializer
    authentication_classes = (
        JSONWebTokenAuthentication, SessionAuthentication)
    permission_classes = [DjangoModelPermissions]

    @action(detail=False, methods=['post'])
    def demais(self, request):
        """\nEndpoint para vincular Endereço a um Cliente\n"""
      
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
            Enderecos.objects.filter(id_cliente=cliente, principal=True).update(principal=False)

            #vincula o endereço ao cliente
            endereco.id_cliente = cliente

            #define o endereço como principal
            endereco.principal = True

            endereco.id_user_cad = request.user
            endereco.save()

            return Response({'message':'Endereço principal atribuido ao cliente '+cliente.nome+' com sucesso!!'})
        except:
            return Response({'message':'Endereço ou cliente não encontrado'}, status=404)


# view com o CRUD de Bairros
class BairrosViewSet(viewsets.ModelViewSet):
    queryset = Bairros.objects.all()
    serializer_class = BairroSerializer
    pagination_class = CustomPagination
    authentication_classes = (
        JSONWebTokenAuthentication, SessionAuthentication)
    permission_classes = [DjangoModelPermissions]

    
    #método para aplicar filtros de Bairros
    def get_queryset(self):   
        bairros = Bairros.objects.all()
        nome_cidade = self.request.query_params.get(
            'nome_cidade', None)
        nome_bairro = self.request.query_params.get(
            'nome_bairro', None)
        nome_uf = self.request.query_params.get(
            'nome_uf', None)
        regiao = self.request.query_params.get(
            'regiao', None)
        
        if nome_cidade:
            bairros = bairros.filter(nome_bairro__icontains=nome_bairro)

        if nome_cidade:
            bairros = bairros.filter(id_cidade__nome_cidade__icontains=nome_cidade)

        if nome_uf:
            bairros = bairros.filter(id_cidade__id_uf__nome_uf__icontains=nome_uf)

        if regiao:
            bairros = bairros.filter(id_cidade__id_uf__regiao__icontains=regiao)
        
        return bairros.order_by('nome_bairro')


# view para listar as cidades, e assim instanciar bairros
class CidadesViewSet(mixins.ListModelMixin,
                     viewsets.GenericViewSet):
    queryset = Cidades.objects.all()
    serializer_class = CidadeSerializer
    authentication_classes = (
        JSONWebTokenAuthentication, SessionAuthentication)
    permission_classes = [DjangoModelPermissions]
    pagination_class = CustomPagination
   
    #método para aplicar filtros de cidades
    def get_queryset(self):   
        cidades = Cidades.objects.all()
        nome_cidade = self.request.query_params.get(
            'nome_cidade', None)
        nome_uf = self.request.query_params.get(
            'nome_uf', None)
        regiao = self.request.query_params.get(
            'regiao', None)
        
        if nome_cidade:
            cidades = cidades.filter(nome_cidade__icontains=nome_cidade)

        if nome_uf:
            cidades = cidades.filter(id_uf__nome_uf__icontains=nome_uf)

        if regiao:
            cidades = cidades.filter(id_uf__regiao__icontains=regiao)
        
        return cidades.order_by('nome_cidade')

