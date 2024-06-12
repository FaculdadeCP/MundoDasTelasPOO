from flask import Blueprint, render_template, request, redirect, url_for, session, flash

funcionario_bp = Blueprint('funcionario', __name__) # Rota para importar no main

@funcionario_bp.route('/funcionario/cadastro') # Rota do site
def funcionario_cadastro(): 
    return render_template('funcionario_cadastro.html') # Página que vai redirecionar


@funcionario_bp.route('/funcionario_consulta.html') # Rota do site
def funcionario_consulta(): 
    return render_template('funcionario_consulta.html') # Página que vai redirecionar
 