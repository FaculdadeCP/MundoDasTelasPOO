from flask import Blueprint, render_template, request, redirect, url_for, session, flash

fornecedor_cadastro_bp = Blueprint('fornecedor', __name__) # Rota para importar no main

@fornecedor_cadastro_bp.route('/fornecedor/cadastro') # Rota do site
def fornecedor_cadastro(): 
    return render_template('fornecedor_cadastro.html') # Página que vai redirecionar

@fornecedor_cadastro_bp.route('/fornecedor/consulta') # Rota do site
def fornecedor_consulta(): 
    return render_template('fornecedor_consulta.html') # Página que vai redirecionar
