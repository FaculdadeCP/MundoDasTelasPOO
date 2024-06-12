from flask import Blueprint, render_template, request, redirect, url_for, session, flash

funcionario_cadastro_bp = Blueprint('funcionario', __name__) # Rota para importar no main

@funcionario_cadastro_bp.route('/funcionario/cadastro') # Rota do site
def funcionario_cadastro(): 
    return render_template('funcionario_cadastro.html') # Página que vai redirecionar
