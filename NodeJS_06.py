from flask import Flask, abort

app = Flask(__name__)

@app.route('/listar/<int:parametro>')
def listar(parametro):
    if parametro == 10:
        return "Conteúdo para o parâmetro 10", 200
    elif parametro == 50:
        abort(404)
    else:
        abort(400)

if __name__ == '__main__':
    app.run(debug=True)
