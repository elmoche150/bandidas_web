from flask import Blueprint, jsonify
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