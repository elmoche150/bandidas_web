from flask import Blueprint, render_template
import os

menu_bp = Blueprint("menu_bp",__name__)

@menu_bp.route('/')
def menu():
    return render_template('menu.html')
