from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "mensagem": "Minha API Flask rodando com sucesso na Azure!",
        "status": "producao",
        "ci_cd": "GitHub Actions funcionando redondinho"
    })

if __name__ == "__main__":
    app.run()