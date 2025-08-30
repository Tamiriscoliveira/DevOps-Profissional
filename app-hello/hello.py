from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Minha Primeira Aplicação em Python com Dockerfile!"