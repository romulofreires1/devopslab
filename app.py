from flask import Flask
from flask_wtf.csrf import CSRFProtect
import os
app = Flask(__name__)

csrf = CSRFProtect(app)

@app.route("/")
def pagina_inicial():
    return "Laboratório DevOps - FIAP 8ASO - GRUPO 11 - SOLUTION SPRINT"

if __name__ == '__main__':
    port = os.getenv('PORT')
    app.run()