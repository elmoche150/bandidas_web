from flask import Blueprint, render_template, request, jsonify, session
import os

nueva_comanda_bp = Blueprint("nueva_comanda_bp",__name__)

@nueva_comanda_bp.route("/nueva", methods=["GET"])
def nueva_comanda():

    if "items" not in session:
        session["items"] = []
    return render_template("nueva_comanda.html")


@nueva_comanda_bp.route("/agregar_item", methods=["POST"])
def agregar_item():
    data = request.get_json()

    item = {
        "producto_id": data["producto_id"],
        "nombre": data["nombre"],
        "cantidad": data["cantidad"],
        "detalles": data.get("detalles", "")
    }

    items = session.get("items", [])
    items.append(item)
    session["items"] = items

    return jsonify({"ok": True, "items": items})


@nueva_comanda_bp.route("/confirmar", methods=["POST"])
def confirmar_comanda():
    items = session.get("items", [])

    if not items:
        return jsonify({"error": "Comanda vacía"}), 400
    
    session.pop("items")

    return jsonify({
        "ok": True,
        "mensaje": "Comanda enviada",
        "items": items
    })