from django.contrib import admin
from .models import *

class DadosCadForm(admin.ModelAdmin):
    readonly_fields = ['cad_por','alt_por']  
    exclude = ['id_user_cad', 'id_user_alt','dt_alt']
    def cad_por(self, instance):
        return str(instance.id_user_cad.first_name + ' ' + instance.id_user_cad.last_name) + ' em ' + instance.dt_cad.strftime('%d/%m/%Y')

    def alt_por(self, instance):
        return str(instance.id_user_alt.first_name + ' ' + instance.id_user_alt.last_name) + ' em ' + instance.dt_alt.strftime('%d/%m/%Y')
    cad_por.short_description = "Cadastrado por"
    alt_por.short_description = "Alterador por"

    def save_model(self, request, obj, form, change):
        if change:
            obj.id_user_alt = request.user
        else:
            obj.id_user_cad = request.user
        obj.save()

    #loop para inserir os dados cad no inline
    def save_formset(self, request, form, formset, change):
        for f in formset.forms:
            try:
                print(f.instance.id_user_cad)
                f.instance.id_user_alt = request.user  
            except:
                try:
                    f.instance.id_user_cad = request.user
                except:
                    print("o objeto nao possui dados cad")
    
        formset.save()


class EnderecosInline(admin.TabularInline):
    model = Enderecos
    extra = 1
    exclude = ['id_user_alt','id_user_cad']
    autocomplete_fields = ['id_bairro']
    fieldsets = (
        ('Endereço', {'fields': ['principal','logradouro','numero','complemento','cep','id_bairro',"tel1"]}),)


class ClienteForm(DadosCadForm):
    list_display = ('nome', 'ativo',)
    list_filter = ( 'ativo',)
    search_fields = ('id_cliente', 'nome')
    raw_id_fields = ['id_user']
    inlines = [EnderecosInline]
    fieldsets = (
        ('Dados básicos', {'fields': (('nome', 'cpf', 'sexo',),
                                      ('email', 'id_user', ),
                                      ('data_nascimento'),)}),

        ('Outros', {
            'classes': ('collapse',),
            'fields':  ('cad_por', 'observacoes', ('alt_por',  'ativo'),), })

    )
class BairrosForm(admin.ModelAdmin):
    search_fields = ['nome_bairro']

admin.site.register(Clientes, ClienteForm)
admin.site.register(Enderecos, DadosCadForm)
admin.site.register(Bairros, BairrosForm)
admin.site.register(Cidades)
admin.site.register(Ufs)
admin.site.register(Paises)
