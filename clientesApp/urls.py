from rest_framework import routers
from .views import *
clienteRoutes = routers.DefaultRouter()

clienteRoutes.register(r'users', UserViewSet)
clienteRoutes.register(r'clientes', ClienteViewSet)
clienteRoutes.register(r'enderecos', EnderecoViewSet)
clienteRoutes.register(r'atribui_enderecos', AtribuiViewSet)
