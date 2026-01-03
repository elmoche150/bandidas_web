from flask import Blueprint, render_template
import os

historial_comandas_bp = Blueprint("historial_comandas_bp",__name__)

@historial_comandas_bp.route('/')
def historial_comandas():
    return render_template('historial_comandas.html')
