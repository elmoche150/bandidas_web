from flask import Blueprint, jsonify
import json
from routes.db.db import get_connection

historial_comandas_bp = Blueprint("historial_comandas_bp", __name__)

# historial_comandas.py (Back)
@historial_comandas_bp.route("/historial_comandas") # Sin el /api/
def historial_api():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    
    query = """
        SELECT c.id, c.fecha_creacion, c.estado,
               JSON_ARRAYAGG(JSON_OBJECT(
                   'nombre', m.nombre,
                   'cantidad', ci.cantidad,
                   'detalles', ci.detalles
               )) AS items
        FROM comandas c
        INNER JOIN comanda_items ci ON c.id = ci.comanda_id
        INNER JOIN menu m ON ci.producto_id = m.id
        GROUP BY c.id
        ORDER BY c.fecha_creacion ASC
    """
    cursor.execute(query)
    comandas = cursor.fetchall()
    
    # Procesamos el JSON antes de enviarlo
    for c in comandas:
        if isinstance(c['items'], str):
            c['items'] = json.loads(c['items'])
            
    cursor.close()
    conn.close()
    return jsonify(comandas)

@historial_comandas_bp.route("/comandas/<int:id>/finalizar", methods=["PATCH"])
def finalizar_comanda(id):
    conn = get_connection()
    cursor = conn.cursor()
    
    try:
        # Actualizamos el estado y la fecha de finalización
        query = "UPDATE comandas SET estado = 'terminada', fecha_finalizacion = NOW() WHERE id = %s"
        cursor.execute(query, (id,))
        conn.commit()
        
        return jsonify({"success": True, "message": "Comanda terminada"}), 200
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"success": False, "message": str(e)}), 500
    finally:
        cursor.close()
        conn.close()