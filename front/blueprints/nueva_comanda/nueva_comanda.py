from flask import Blueprint, render_template
import os

nueva_comanda_bp = Blueprint("nueva_comanda_bp",__name__)

@nueva_comanda_bp.route('nueva_comanda')
def nueva_comanda():
    return render_template('nueva_comanda.html')
