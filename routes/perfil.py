# routes/perfil.py
from flask import Blueprint, render_template, session, redirect, url_for

perfil_bp = Blueprint('perfil', __name__)

@perfil_bp.route('/perfil')
def perfil():
    if not session.get('logged_in'):
        return redirect(url_for('acesso.login'))
    return render_template('perfil.html')
