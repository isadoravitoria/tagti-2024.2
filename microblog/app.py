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
    return "isadora.vitoria@aluno.ifsertao-pe.edu.br"

if __name__ == '__main__':
    app.run()
