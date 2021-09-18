from rest_framework import routers
from .views import *
clienteRoutes = routers.DefaultRouter()

clienteRoutes.register(r'user', UserViewSet)
clienteRoutes.register(r'cliente', ClienteViewSet)
clienteRoutes.register(r'endereco', EnderecoViewSet)
