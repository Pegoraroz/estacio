from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return ('Página principal')

@app.route('/ola/')
def ola_mundo():
    return ('Olá, mundo!')

@app.route('/ola/<nome>')
def nome_do_usuario(nome = "mundo"):
    return ("Olá, " + nome)

if __name__ == '__main__':
    app.run()