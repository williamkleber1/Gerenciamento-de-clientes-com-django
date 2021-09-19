
from django.test import TestCase
import datetime

from clientesApp.serializers import *


class UserTestCase(TestCase):

    def setUp(self):
        user = User.objects.create(  username='usertest01',
                                     email='teste@mail.com',
                                     password='1234teste',
                                     is_staff=True,
                                     is_superuser=False)

    def test_dados_user(self):
        p1 = User.objects.get(username='usertest01')
        self.assertEquals(p1.username, 'usertest01')
        self.assertEquals(p1.email,'teste@mail.com')
        self.assertEquals(p1.is_staff,True)
        self.assertEquals(p1.is_superuser,False)


class ClientesTestCase(TestCase):

    def setUp(self):
        user = User.objects.create(username='usertest1')
        Clientes.objects.create(**{
                "nome": "william kleber alves dos santos",
                "cpf": "45236273947634",
                "sexo": "M",
                "email": "williamkleb@hotmail.com",
                "data_nascimento": "2021-09-18",
                "observacoes": "Teste de model",
                "ativo": True,
                "id_user_cad": user,
                "id_user": user
                }
        )

    def test_retorno_str(self):
        p1 = Clientes.objects.get(nome='william kleber alves dos santos')
        self.assertEquals(p1.__str__(), 'william kleber alves dos santos')

    def test_dados_model_Clientes(self):
        p1 = Clientes.objects.get(nome='william kleber alves dos santos')
        self.assertEquals(p1.nome, 'william kleber alves dos santos')
        self.assertEquals(p1.cpf, '45236273947634')
        self.assertEquals(p1.sexo, 'M')
        self.assertEquals(p1.data_nascimento, datetime.datetime.strptime('2021/09/18', '%Y/%m/%d').date())
        self.assertEquals(p1.observacoes, 'Teste de model')
        self.assertEquals(p1.ativo, True)

class EnderecoTestCase(TestCase):

    def setUp(self):
        uf = Ufs.objects.create(nome_uf='Alagoas', sigla_uf='AL', regiao='Nordeste')
        cidade = Cidades.objects.create(id_uf=uf, nome_cidade='Maceió')
        bairro = Bairros.objects.create(id_cidade=cidade, nome_bairro='Centro')
        user = User.objects.create(username='usertest1')
        cliente = Clientes.objects.create(**{
                "nome": "william kleber alves dos santos",
                "cpf": "45236273947634",
                "sexo": "M",
                "email": "williamkleb@hotmail.com",
                "data_nascimento": "2021-09-18",
                "observacoes": "Teste de model",
                "ativo": True,
                "id_user_cad": user,
                "id_user": user
                })

        Enderecos.objects.create(**{"logradouro":"Rua dos bobos",
                                    "numero":"0",
                                    "complemento":"onde o vento faz curvas",
                                    "cep":"00000000",
                                    "tel1":"857343384",
                                    "observacoes": "Teste de endereço",
                                    "principal": False,
                                    "id_user_cad": user,
                                    "id_cliente": cliente,
                                    "id_bairro": bairro
                                    
                                    })

    def test_dados_endereco(self):
        e1  = Enderecos.objects.get(logradouro='Rua dos bobos', numero='0')
        self.assertEquals(e1.logradouro, 'Rua dos bobos')
        self.assertEquals(e1.numero,'0')
        self.assertEquals(e1.cep,"00000000")
        self.assertEquals(e1.tel1,"857343384")
        self.assertEquals(e1.observacoes,"Teste de endereço")
        self.assertEquals(e1.principal,False)
        self.assertEquals(e1.id_cliente.nome,"william kleber alves dos santos")
        self.assertEquals(e1.id_bairro.nome_bairro,'Centro')
        self.assertEquals(e1.id_bairro.id_cidade.nome_cidade,'Maceió')
        self.assertEquals(e1.id_bairro.id_cidade.id_uf.nome_uf,'Alagoas')




        
