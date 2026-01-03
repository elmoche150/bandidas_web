from flask import Blueprint, request, jsonify
from routes.db.db import get_connection

nueva_comandas_bp = Blueprint("nueva_comandas_bp", __name__)

@nueva_comandas_bp.route("/comandas", methods=["POST"])
def crear_comanda():
    data = request.get_json()
    items = data.get("items", [])

    if not items:
        return jsonify({"error": "Comanda vacía"}), 400

    conn = get_connection()
    cursor = conn.cursor()

    # Crear comanda
    cursor.execute("INSERT INTO comandas () VALUES ()")
    comanda_id = cursor.lastrowid

    # Crear items
    for item in items:
        cursor.execute("""
            INSERT INTO comanda_items
            (comanda_id, producto_id, cantidad, detalles)
            VALUES (%s, %s, %s, %s)
        """, (
            comanda_id,
            item["producto_id"],
            item["cantidad"],
            item.get("detalles", "")
        ))

    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({"mensaje": "Comanda creada", "id": comanda_id}), 201