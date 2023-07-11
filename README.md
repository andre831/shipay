# Shipay API

## Resumo

API desenvolvida em Python utilizando framework Flask para construção das requisições, SQL Alchemy para migração e manipulação de dados.

Hospedagem da aplicação: [Link da API](https://shipay-emkujpq4cq-uc.a.run.app/)

Objetivo da API:

- Listar e criar usuários
- Listar e criar funções

## Definindo o ambiente de desenvolvimento

- Crie um ambiente virtual:

  `python3 -m venv .venv`

- Ative o ambiente virtual:

  `source .venv/bin/activate`

  (Para desativar use `deactive`)

- Ainda na raiz do projeto, instale todas as dependências necessárias:

  `pip install -r requirements.txt`

- Rode os containeres necessários:

  `docker-compose -f dev-compose.yml build | docker-compose -f dev-compose.yml up`

- Para a migração dos dados, utilize:

  - `flask db migrate`
  - `flask db upgrade`

## Deploy

Para fazer o deploy desse projeto rode, é necessário apenas que seja feito um push na branch `main`

```bash
    git push origin main
```

### Como funciona o deploy?

    Armazenado no Google Cloud Plataform, está sendo usado o recurso de Clound Run, serviço que permite manter em funcionamento uma aplicação sem a necessidade de servidor.

    É necessário um `Dockerfile` que irá gerar a imagem necessária para rodar um container com a aplicação.

    Com este recurso é possível fazer a implementação automática de novos recursos sempre que realizar um commit no projeto.

##

## Rotas da API

#### Retorna todos os usuários

```http
  GET /users
```

#### Retorna a função de um usuário

```http
  GET /users/<user_id>/role/<role_id>
```

| Parâmetro | Tipo     | Descrição                                  |
| :-------- | :------- | :----------------------------------------- |
| `user_id` | `string` | **Obrigatório**. O ID do usuário           |
| `role_id` | `string` | **Obrigatório**. O ID da função do usuário |

#### Registrar novo usuário

```http
  POST /users
```

    Corpo da requisição(exemplo):

    {
        "name": João Pé de Feijão
        "email": joao@pe.de.feijao
        "password": "joao123"
        "role_id": 1
    }

    OBS: caso não seja passado a chave password, será gerada automaticamente.

#### Retorna todas as funções registradas

```http
  GET /roles
```

#### Registrar nova função

```http
  POST /roles/new
```

    Corpo da requisição(exemplo):

        {
            "description": "Gerente"
        }

## Arquitetura

- `src`:

  Armazena todas as funcionalidades da aplicação

  - `model`:

    Camada responsável pela construção das tabelas do banco de dados;

  - `database`:

    Classes mais próximas do banco de dados, onde serão trazidos todos dados;

  - `controller`:

    Classes responsáveis pelo tratamento dos dados e regras de negócios caso necessário;

  - `routes`:

    Camada onde serão definidas as rotas para a realização das requisições.

  - `app.py`:

    Arquivo core da aplicação, onde serão definos as configurações necessárias do projeto.

- `requirements.txt`:
  Arquivo onde deve ser registrado todas as dependências do projeto.

- `Dockerfile`:
  Arquivo necessário para que seja deployado o projeto corretamente, além disso, cria a imagem necessária para o container de desenvolviment.

- `dev-compose.yml`:
  Armazena configurações para uso do projeto no ambiente local.

## Banco de dados

    O banco de dados usado na aplicação é PostgreSQL, armazenado em um cluster cloud separadamente.

    [Banco de dados aqui!](https://clients.cloudclusters.io/applications/ce24ff9063e04c27aa5c8bac92fe8468/dbuser)
