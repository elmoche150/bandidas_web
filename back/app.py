from flask import Flask
from flask_cors import CORS
import os

from routes.menu.menu import menu_bp
from routes.nueva_comanda.nueva_comanda import nueva_comandas_bp
from routes.historial_comandas.historial_comandas import historial_comandas_bp

app = Flask(__name__)

app.register_blueprint(menu_bp)
app.register_blueprint(nueva_comandas_bp)
app.register_blueprint(historial_comandas_bp)

CORS(app)

@app.route('/')
def index():
    return {"message": "API funcionando"}, 200

if __name__ == "__main__":
    app.run("localhost", port=5006, debug=True)