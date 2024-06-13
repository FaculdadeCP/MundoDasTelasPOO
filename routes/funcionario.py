from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from classes.cls_Funcionario import  Funcionario

funcionario_bp = Blueprint('funcionario', __name__) # Rota para importar no main

@funcionario_bp.route('/funcionario/cadastro') # Rota do site
def funcionario_cadastro(): 
    return render_template('funcionario_cadastro.html') # Página que vai redirecionar


@funcionario_bp.route('/funcionario_consulta')
def funcionario_consulta():
    funcionarios = Funcionario.CarregarFuncionarios()  # Carrega dados dos funcionários
    return render_template('funcionario_consulta.html', funcionarios=funcionarios)
 