# Gerenciamento de clientes com django
 
![GitHub repo size](https://img.shields.io/github/repo-size/williamkleber1/Gerenciamento-de-clientes-com-django?style=for-the-badge)
![GitHub language count](https://img.shields.io/github/languages/count/williamkleber1/Gerenciamento-de-clientes-com-django?style=for-the-badge)
![GitHub forks](https://img.shields.io/github/forks/williamkleber1/Gerenciamento-de-clientes-com-django?style=for-the-badge)
![Bitbucket open issues](https://img.shields.io/github/issues/williamkleber1/Gerenciamento-de-clientes-com-django?style=for-the-badge)


<img src="https://leads2b.com/blog/wp-content/uploads/2020/12/capa-Fidelizacao-de-clientes.png" alt="exemplo imagem">

> Aplicação para a gestão de clientes.

## 📚 Documentação


[Github Projects](https://gwilliamkleber1/Gerenciamento-de-clientes-com-django/projects/1)  : Kanbam com as tarefas de implementação, documentação e issues


[Modelo ER](https://github.com/williamkleber1/Gerenciamento-de-clientes-com-django/blob/main/documentation/modelo_er.png) : Modelo de entidade e relacionamento do projeto



## 🚀 Executando Gerenciador

Para executar o Gerenciador, siga estas etapas:

Baixe o repositório :
```
git clone https://github.com/williamkleber1/Gerenciamento-de-clientes-com-django.git
```
Abra o diretorio do projeto:
```
cd Gerenciamento-de-clientes-com-django
```

Inicialize o projeto usando o docker:
```
docker-compose up -d 
```

a aplicação estará rodando em :
```
http://0.0.0.0:8000/
```
#### Popular Tabelas Ufs, Cidades e Bairros com dados predefinidos( OPCIONAL)

abrir o bash do container do django:
```
docker exec -it django_clientes bash
```

executar o shell do django:
```
python manage.py shell
```

importar a função popular_banco():
```
from clientesApp.helper import *
```

executar a função popular_banco():
```
popular_banco()
```


## 🤝 Colaboradores


<table>
  <tr>
    <td align="center">
      <a href="#">
        <img src="https://avatars.githubusercontent.com/u/26510655?v=4" width="100px;" alt="Foto do William Kleber"/><br>
        <sub>
          <b>William Kleber</b>
        </sub>
      </a>
    </td>
  </tr>
</table>


