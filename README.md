# PostPythonAPI

Esta é uma API simples para gerenciar séries de TV. Ela permite listar, adicionar, atualizar e excluir séries do banco de dados.

## Requisitos
Para executar a API, você precisará das seguintes ferramentas instaladas em sua máquina:

- Python 3.x
- Flask
- PostgresSQL (ou outro banco de dados compatível com psycopg2)

## Configuração do Banco de Dados
Antes de executar a API, você deve configurar o banco de dados. Para isso, crie um banco de dados PostgreSQL e execute o seguinte script SQL para criar a tabela necessária:

```sql
Copy code
CREATE TABLE series (
    id SERIAL PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    genre VARCHAR(50),
    num_episodes INTEGER,
    release_year INTEGER
);
```

Coloque os dados de conexão do seu Postgres em `config.py`:
```python
# Configurações do banco de dados PostgreSQL
db_config = {
    "dbname": "series",
    "user": "<seu_user_name>",
    "password": "<seu_password>",
    "host": "localhost",
    "port": "5432",
    "client_encoding": "UTF8"  # Adicione esta linha para definir a codificação UTF-8
}
```

## Instalação

- Clone este repositório para o seu computador
- Navegue até o diretório do projeto:
```python
python -m venv env
```

### Ativação:

Windows:
```
env\Scripts\activate
```

Linux/Mac:
```
source env/bin/activate
```

Instale as dependências:
```
pip install -r requirements.txt
```

## Executando a API

Para executar a API, use o seguinte comando:

```
python app.py
```

A API estará disponível em http://localhost:5000.

## Rotas

-GET /series: Retorna todas as séries cadastradas no banco de dados.

- GET /series/{id}: Retorna os detalhes de uma série específica com base no ID fornecido.

- POST /series: Adiciona uma nova série ao banco de dados. Você deve fornecer os dados da série em formato JSON no corpo da solicitação.

- PUT /series/{id}: Atualiza os dados de uma série existente com base no ID fornecido. Você deve fornecer os dados atualizados da série em formato JSON no corpo da solicitação.

- DELETE /series/{id}: Exclui uma série específica com base no ID fornecido.

## Testando a API
Para inserir valores de teste no banco de dados, execute o arquivo insert_test_data.py. Certifique-se de estar no ambiente virtual antes de executar o comando:

```python
python insert_test_data.py
```

Isso inserirá algumas séries de teste no banco de dados.

## Contribuição
Se você quiser contribuir para este projeto, sinta-se à vontade para abrir um pull request.
