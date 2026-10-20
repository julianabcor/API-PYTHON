# Desenvolver um backend com API 
# Postman - testes HTTP -> verificar respostas da API
# 1. Objetivo
# 2. URL base
# 3. ENDPOINTS
# 4. Recursos disponibilizados

# Vamos criar uma API:

""" 
1. CONSULTAR
2. CRIAR
3. EDITAR
4. EXCLUIR
C.R.U.D
"""

from flask import Flask, jsonify, request 

app = Flask(__name__)
# app -> representa a aplicação flask
#__name__ identifica o módulo da aplicação

livros = [
    {"id": 1,
     "titulo": "Percy Jackson",
     "autor": "Rick Riordan"
     },

    {"id": 2,
     "titulo": "Harry Potter",
     "autor": "J.K ROWLING"
     },

    {"id": 3,
     "titulo": "É assim que acaba",
     "autor": "Colleen Hover"
     },

    {"id": 4,
     "titulo": "O Senhor dos Anéis",
     "autor": "J.R.R. Tolkien"
     },

    {"id": 5,
     "titulo": "1984",
     "autor": "George Orwell"
     },

    {"id": 6,
     "titulo": "Dom Casmurro",
     "autor": "Machado de Assis"
     },

    {"id": 7,
     "titulo": "O Pequeno Príncipe",
     "autor": "Antoine de Saint-Exupéry"
     },

    {"id": 8,
     "titulo": "A Culpa é das Estrelas",
     "autor": "John Green"
     },

    {"id": 9,
     "titulo": "Jogos Vorazes",
     "autor": "Suzanne Collins"
     },

    {"id": 10,
     "titulo": "O Hobbit",
     "autor": "J.R.R. Tolkien"
     },

    {"id": 11,
     "titulo": "A Revolução dos Bichos",
     "autor": "George Orwell"
     },

    {"id": 12,
     "titulo": "Capitães da Areia",
     "autor": "Jorge Amado"
     },

    {"id": 13,
     "titulo": "O Código Da Vinci",
     "autor": "Dan Brown"
     },
]

# Consultar livros (criar uma função)
#def obter_livros():
    #return jsonify(livros)

# Criar as rotas /livros
# A rota foi especificada, somente o método GET será aceito
@app.route("/livros",methods =["GET"])
def obter_livros():
    return jsonify(livros)

# Criar rota /livrosid
@app.route("/livros/<int:id>",methods=["GET"])
#<int:> -> indica inteiro 
def obter_livro_por_id(id):
    for livro in livros:
        if livro.get("id") == id:
            return jsonify(livro)
    return jsonify({"message":"Livro não encontrado!"}), 404

# PUT -> primeiro, os dados enviados pelo cliente serão obtidos 
@app.route("/livros/<int:id>",methods=["PUT"])
def editar_livro_por_id(id):
    #permite acessar os dados json enviados no corpo da requisição
    livro_alterado = request.get_json()
    for indice, livro in enumerate(livros):
        if livro.get("id")==id:
            livros[indice].update(livro_alterado)
            return jsonify(livro[indice])

# Criação de um novo livro
@app.route("/livros", methods=["POST"])
def incluir_novo_livro():
    novo_livro = request.get_json()
    livros.append(novo_livro)

    return jsonify(livros)

# Delete - excluir um livro
@app.route("/livros/<int:id>", methods=["DELETE"])
def excluir_livro(id):
    # Como é necessário excluir um elemento da lista pelo seu indice, será utilizado novamente o enumerate()
    for indice, livro in enumerate(livros):
        if livro.get("id") == id:
            livros.pop(indice)
            return jsonify(livros)

# Inicialização do servidor local
app.run(
    host="localhost",
    port=5000,
    debug=True
)