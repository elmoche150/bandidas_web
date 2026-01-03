from flask import Flask
from flask_cors import CORS
import os
import socket

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


def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('8.8.8.8', 1)) # No necesita internet, solo para detectar la interfaz
        ip = s.getsockname()[0]
    except Exception:
        ip = '127.0.0.1'
    finally:
        s.close()
    return ip

if __name__ == "__main__":

    local_ip = get_local_ip()
    print(f"--- SERVIDOR ACTIVO EN LA RED ---")
    print(f"IP para la otra PC: http://{local_ip}:5006")
    print(f"---------------------------------")
    # Escucha en 0.0.0.0 para ser visible en el WiFi
    app.run("0.0.0.0", port=5006, debug=True)