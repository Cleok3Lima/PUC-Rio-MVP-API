# Gestão de Tempo API

## Descrição

<p align="center">
  <img alt="Cleok3-pic" width="300" src="https://cdn.discordapp.com/attachments/1217082427021725849/1256996429528825866/cleolimadev_1.png?ex=6682cca6&is=66817b26&hm=4b1248106917647f3ee387ca82efd4c732cbe5e5aaeb8fca29a7cd3ae8e079f3&">
</p>

A Gestão de Tempo API é uma aplicação backend desenvolvida em Python utilizando o framework Flask. A API permite gerenciar tarefas diárias, monitorar o tempo e analisar a produtividade. A aplicação inclui funcionalidades como criar tarefas, marcar tarefas como concluídas, deletar tarefas e visualizar todas as tarefas.

## Índice

- [Tecnologias](#tecnologias)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Instalação](#instalação)
- [Uso](#uso)
- [Rotas da API](#rotas-da-api)
- [Contribuição](#contribuição)
- [Licença](#licença)

## Tecnologias

- Python 3.12
- Flask
- SQLite
- Flask-CORS
- Flask-JWT-Extended
- Flask-SQLAlchemy
- Flask-CORS
- Flask-OpenAPI3
- Flask-Swagger-UI

## Estrutura do Projeto

```
gestao-tempo-api/
├── instance/
│   ├── tabelas.db
├── model/
│   ├── __init__.py
│   ├── base.py
│   ├── tarefa.py
│   ├── usuario.py
├── schemas/
│   ├── __init__.py
│   ├── error.py
│   ├── tarefa.py
│   ├── usuario.py
├── static/
│   ├── swagger.json
├── .gitignore
├── app.py
├── log_config.py
├── README.md
└── requirements.txt
```

## Configuração e Execução

## Instalação

1. Clone o repositório:

   ```sh
   git clone https://github.com/Cleok3Lima/PUC-Rio-MVP-API.git
   cd gestao-de-tempo-api
   ```

2. Crie um ambiente virtual e ative-o:

   ```sh
   python -m venv .venv
   source .venv/bin/activate  # No Windows use: .venv\Scripts\activate
   ```

3. Instale as dependências:

   ```sh
   pip install -r requirements.txt
   ```

4. Configure a variável de ambiente para a chave secreta do JWT:

   ```sh
   export JWT_SECRET_KEY='sua-chave-secreta'  # No Windows use: set JWT_SECRET_KEY='sua-chave-secreta'
   ```

5. Execute a aplicação:
   ```sh
   python app.py
   ```

## Uso

A aplicação estará disponível em `http://localhost:8000`. A documentação Swagger (OpenAPI) pode ser acessada em `http://localhost:8000/openapi`.

## Rotas da API

### Usuário

- `POST /register`: Registrar um novo usuário

  - Corpo da solicitação:
    ```json
    {
      "username": "seu_usuario",
      "password": "sua_senha"
    }
    ```

- `POST /login`: Fazer login
  - Corpo da solicitação:
    ```json
    {
      "username": "seu_usuario",
      "password": "sua_senha"
    }
    ```

### Tarefas

- `GET /tarefas`: Obter todas as tarefas do usuário logado
- `POST /tarefas`: Criar uma nova tarefa

  - Corpo da solicitação:
    ```json
    {
      "title": "Título da tarefa",
      "description": "Descrição da tarefa",
      "due_date": "dd/mm/yyyy"
    }
    ```

- `DELETE /tarefas/<int:tarefa_id>`: Deletar uma tarefa
- `POST /tarefas/<int:tarefa_id>/complete`: Marcar uma tarefa como concluída

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e pull requests para melhorar esta aplicação.

## Licença

Este projeto está licenciado sob a Licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.
