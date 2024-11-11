#python -m venv venv
#.\venv\Scripts\activate
#pip install flask
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route("/contato")
def contato():
    return render_template("contato.html", tel= "(87) 988445785",nome= "Isadora")


@app.route("/user/<nome>/<sobrenome>")
def user(nome,sobrenome):
    return f"Olá, {nome} {sobrenome}!"

# Calculadora para somar dois números passados po parâmetro
#@app.route("/soma/<int:num1>/<int:num2>")

#Minha pagina pessoal
@app.route('/sobre')
def sobre():
    return render_template("sobre.html")

if __name__ == '__main__':
    app.run()
