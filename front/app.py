from flask import Flask, render_template
from dotenv import load_dotenv
import os

from blueprints.index.index import index_bp
from blueprints.nueva_comanda.nueva_comanda import nueva_comanda_bp
from blueprints.historial_comandas.historial_comandas import historial_comandas_bp


load_dotenv()
app = Flask(__name__)
app.secret_key = "clave-super-secreta"


app.register_blueprint(index_bp, url_prefix="/")
app.register_blueprint(nueva_comanda_bp, url_prefix="/nueva_comanda")
app.register_blueprint(historial_comandas_bp, url_prefix="/historial_comandas")


if __name__  == "__main__":
    app.run("localhost", port= "5003", debug=True)