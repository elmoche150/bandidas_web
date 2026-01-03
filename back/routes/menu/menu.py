from flask import Blueprint, jsonify, request
from routes.db.db import get_connection

menu_bp = Blueprint("menu_bp", __name__)
@menu_bp.route("/menu", methods=["GET"])
def get_menu():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT id, nombre, estado FROM menu")
    data = cursor.fetchall()
    conn.close()
    return jsonify(data)

@menu_bp.route("/menu_agregar", methods=["POST"])
def agregar_al_menu():
    data = request.json
    nombre = data.get('nombre')
    precio = data.get('precio')
    estado = data.get('estado')

    conn = get_connection()
    cursor = conn.cursor()
    try:
        query = "INSERT INTO menu (nombre, precio, estado) VALUES (%s, %s, %s)"
        cursor.execute(query, (nombre, precio, estado))
        conn.commit()
        return jsonify({"success": True}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        cursor.close()
        conn.close()