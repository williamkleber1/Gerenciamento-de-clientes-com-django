from django.db import models
from django.contrib.auth.models import User


sexo_choices = [('M', 'Masculino'), ('F', 'Feminino')]




#Classe abstrata para salvar as datas de criação e edição, e usuário que executou a ação
class DadosCadModel(models.Model):
    id_user_cad = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='%(class)s_user_cad', null=True, blank=True)
    dt_cad = models.DateField(auto_now_add=True)
    id_user_alt = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True,blank=True, related_name='%(class)s_user_alt')
    dt_alt = models.DateField(null=True, blank=True, auto_now=True)

    class Meta:
        abstract = True




class Ufs(models.Model):
    id_uf = models.AutoField(primary_key=True)
    nome_uf = models.CharField(max_length=30)
    sigla_uf = models.CharField(max_length=2)
    regiao = models.CharField(max_length=30, null=True)

    class Meta:
        ordering = ['sigla_uf']
        db_table = 'Ufs'
        verbose_name_plural = 'Ufs'

    def __str__(self):
        return self.nome_uf


class Cidades(models.Model):
    id_cidade = models.AutoField(primary_key=True)
    id_uf = models.ForeignKey(Ufs, on_delete=models.CASCADE)
    nome_cidade = models.CharField(max_length=50)

    class Meta:
        ordering = ['nome_cidade']
        db_table = 'Cidades'
        verbose_name_plural = 'Cidades'

    def __str__(self):
        return str(self.nome_cidade) + '/'  + str(self.id_uf.nome_uf)


class Bairros(models.Model):
    id_bairro = models.AutoField(primary_key=True)
    id_cidade = models.ForeignKey(Cidades, on_delete=models.CASCADE)
    nome_bairro = models.CharField(max_length=80)

    class Meta:
        ordering = ['nome_bairro']
        db_table = 'Bairros'
        verbose_name_plural = 'Bairros'

    def __str__(self):
        return self.nome_bairro + ' - ' +self.id_cidade.__str__()


class Clientes(DadosCadModel):
    id_cliente = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=14)
    sexo = models.CharField(max_length=1, default='M', choices=sexo_choices)
    email = models.CharField(max_length=80)
    data_nascimento = models.DateField()
    id_user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='%(class)s_id_user')
   
    observacoes = models.TextField(max_length=4000, null=True, blank=True)
    ativo = models.BooleanField(default=True)
  
    class Meta:
        verbose_name_plural = 'Clientes'
        ordering = ['nome']
        db_table = "Clientes"

    def __str__(self):
        return self.nome

class Enderecos(DadosCadModel):
    id_endereco = models.AutoField(primary_key=True)
    logradouro = models.CharField(max_length=150)
    numero = models.CharField(max_length=8)
    complemento = models.CharField(max_length=60, null=True, blank=True)
    cep = models.CharField(max_length=10)
    id_bairro = models.ForeignKey(Bairros, on_delete=models.CASCADE)
    tel1 = models.CharField(max_length=15)
    observacoes = models.TextField(max_length=10000, null=True, blank=True)
    id_cliente = models.ForeignKey(Clientes, on_delete=models.CASCADE, null=True)
    principal = models.BooleanField(default=False)
    class Meta:
        ordering = ['logradouro']
        db_table = 'Enderecos'
        verbose_name_plural = 'Endereços'

    def __str__(self):
        return self.logradouro + str(self.id_bairro)



