from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'password')

    def create(self, validated_date):
        user = super(UserSerializer, self).create(validated_date)
        #fazendo a hash da senha
        user.set_password(validated_date['password'])
        user.save()
        return user

    def update(self, instance, validated_data):
        #fazendo a hash da senha
        instance.set_password(validated_data['password'])
        instance.username = validated_data['username']
        instance.save()
        return instance

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clientes
        fields = '__all__'

class UfsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ufs
        fields = '__all__'

class CidadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cidades
        fields = '__all__'
        
    def to_representation(self, obj):
        return{
                "id_cidade": obj.id_cidade,
                "nome_cidade": obj.__str__(),
                "id_uf": obj.id_uf.id_uf
            }

class BairroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bairros
        fields = '__all__'

class EnderecoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enderecos
        fields = '__all__'



class AtribuiSerializer(serializers.Serializer):
    id_cliente = serializers.IntegerField(required=True)
    id_endereco = serializers.IntegerField(required=True)


