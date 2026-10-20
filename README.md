# API de Livros 📚

API REST em Python para gerenciar uma coleção de livros. Cada livro possui `id`, `titulo` e `autor`.

## Tecnologias

- Python 3
- Flask

## Funcionalidades

- Listar todos os livros
- Consultar um livro por ID
- Cadastrar um novo livro
- Editar um livro existente
- Excluir um livro

## Como executar

1. Clone o repositório:

```bash
git clone https://github.com/julianabcor/API-PYTHON.git
cd API-PYTHON
```

2. (Opcional) Crie e ative um ambiente virtual:

```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

3. Instale as dependências:

```bash
pip install flask
```

4. Execute a aplicação (troque `app.py` pelo nome do seu arquivo):

```bash
python app.py
```

A API ficará disponível em `http://localhost:5000`.

## Endpoints

| Método | Rota           | Descrição                  |
|--------|----------------|----------------------------|
| GET    | `/livros`      | Lista todos os livros      |
| GET    | `/livros/<id>` | Retorna um livro pelo ID   |
| POST   | `/livros`      | Cadastra um novo livro     |
| PUT    | `/livros/<id>` | Atualiza um livro          |
| DELETE | `/livros/<id>` | Remove um livro            |

## Exemplo de livro

```json
{
  "id": 1,
  "titulo": "Percy Jackson",
  "autor": "Rick Riordan"
}
```

## Exemplos de uso

Listar livros:

```bash
curl http://localhost:5000/livros
```

Cadastrar um livro:

```bash
curl -X POST http://localhost:5000/livros \
  -H "Content-Type: application/json" \
  -d '{"id": 31, "titulo": "Novo Livro", "autor": "Autor Exemplo"}'
```

## Observações

Os dados ficam armazenados em uma lista em memória, então são reiniciados sempre que a aplicação é reiniciada.

## Autora

Desenvolvido por [julianabcor](https://github.com/julianabcor).
