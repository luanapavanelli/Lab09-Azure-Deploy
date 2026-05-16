from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "mensagem": "API Atualizada com Sucesso via CI/CD!",
        "exercicio": "9.4 - Teste de Automacao",
        "status": "Online na Nuvem Azure",
        "autor": "Luana Pavanelli"
    })

# Nova rota para simular um endpoint de produtos/livros
@app.route("/produtos")
def listar_produtos():
    return jsonify([
        {"id": 1, "nome": "Clean Code", "preco": 89.90},
        {"id": 2, "nome": "Arquitetura Limpa", "preco": 95.00},
        {"id": 3, "nome": "Refatoracao", "preco": 120.00}
    ])

if __name__ == "__main__":
    app.run()