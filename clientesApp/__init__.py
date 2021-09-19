from django.db import connection
from .helper import ufs_sql, cidades_sql,bairros_sql

#populando as tabelas Ufs, Cidades e Bairros

try:
    with connection.cursor() as cursor:
        cursor.execute(ufs_sql)
        cursor.execute(cidades_sql)
        cursor.execute(bairros_sql)
    print("SQL de Ufs executado")

except:
    print("Erro ao executar SQL")