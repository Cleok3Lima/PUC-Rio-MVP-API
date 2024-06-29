# Gestão de Tempo API

## Descrição

<style>
img{
    position: relative;
    bottom: 60px;
    float: right;
    width: 300px;
}
</style>

<img alt="Cleok3-pic" src="https://www.cleolima.dev/cleolimadev.svg">

A Gestão de Tempo API é uma aplicação backend desenvolvida em Python utilizando o framework Flask. A API permite gerenciar tarefas diárias, monitorar o tempo e analisar a produtividade. A aplicação inclui funcionalidades como criar tarefas, marcar tarefas como concluídas, deletar tarefas e visualizar todas as tarefas.

## Tecnologias Utilizadas

- Python
- Flask
- SQLite
- Flask-CORS
- Flasgger (para documentação da API com Swagger)
- Logging configurado para monitorar eventos da aplicação

## Estrutura do Projeto

```
gestao-tempo-api/
├── model/
│   ├── __init__.py
│   ├── base.py
│   ├── tarefa.py
├── schemas/
│   ├── __init__.py
│   ├── error.py
│   ├── tarefa.py
├── app.py
├── log_config.py
├── requirements.txt
├── tarefas.db
└── README.md
```

### Pasta log

A pasta log é usada para armazenar arquivos de log gerados pela aplicação. Inicialmente, ela estará vazia, mas será preenchida com arquivos de log conforme a aplicação for executada.

- app.error.log: Armazena logs de erros.
- app.detailed.log: Armazena logs detalhados de todas as atividades.

## Configuração e Execução

### Pré-requisitos

- Python 3.x
- Pip (gerenciador de pacotes do Python)

### Instalação

1. Clone o repositório:

   ```bash
   git clone <URL-do-repositorio>
   cd gestao-tempo-api
   ```

2. Crie um ambiente virtual e ative-o:

   ```bash
   python -m venv .venv
   source .venv/bin/activate   # No Windows use `venv\Scripts\activate`
   ```

3. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

### Execução da Aplicação

1. Inicialize o banco de dados:

   ```bash
   python -c "from app import init_db; init_db()"
   ```

2. Inicie o servidor:

   ```bash
   flask run --host 0.0.0.0 --port 5000
   ```

   Em modo de desenvolvimento é recomendado executar utilizando o parâmetro reload, que reiniciará o servidor automaticamente após uma mudança no código fonte.

   ```bash
   flask run --host 0.0.0.0 --port 5000 --reload
   ```

A aplicação estará disponível em `http://127.0.0.1:5000`.

## Rotas da API

### Cadastrar Tarefa (POST)

- **Endpoint**: `/tarefa`
- **Descrição**: Adiciona uma nova tarefa.
- **Parâmetros**:
  - `titulo` (string): Título da tarefa (obrigatório)
  - `descricao` (string): Descrição da tarefa (opcional)
  - `data_vencimento` (string): Data de vencimento da tarefa (opcional)
- **Exemplo de Request**:

  ```json
  {
    "titulo": "Estudar Flask",
    "descricao": "Estudar o framework Flask para desenvolvimento web",
    "data_vencimento": "2024-07-01"
  }
  ```

- **Exemplo de Response**:

  ```json
  {
    "message": "Tarefa cadastrada com sucesso!"
  }
  ```

### Buscar Tarefas (GET)

- **Endpoint**: `/tarefas`
- **Descrição**: Retorna uma lista de todas as tarefas cadastradas.
- **Exemplo de Response**:

  ```json
  [
    {
      "id": 1,
      "titulo": "Estudar Flask",
      "descricao": "Estudar o framework Flask para desenvolvimento web",
      "data_vencimento": "2024-07-01",
      "concluida": false
    }
  ]
  ```

### Deletar Tarefa (DELETE)

- **Endpoint**: `/tarefa`
- **Descrição**: Deleta uma tarefa pelo ID (Ou pelo título?).
- **Exemplo de Response**:

  ```json
  {
    "message": "Tarefa deletada com sucesso!"
  }
  ```

### Marcar Tarefa como Concluída (PUT)

- **Endpoint**: `/concluir_tarefa`
- **Descrição**: Marca uma tarefa como concluída pelo ID.
- **Exemplo de Response**:

  ```json
  {
    "message": "Tarefa marcada como concluída!"
  }
  ```

## Documentação da API

A documentação da API está disponível através do Swagger. Após iniciar o servidor, acesse a documentação em `http://127.0.0.1:5000/apidocs`.

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e pull requests.

## Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.
