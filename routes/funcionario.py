from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from classes.cls_Funcionario import  Funcionario


funcionario_bp = Blueprint('funcionario', __name__) # Rota para importar no main

@funcionario_bp.route('/funcionario/cadastro') # Rota do site
def funcionario_cadastro(): 
    return render_template('funcionario_cadastro.html') # Página que vai redirecionar


@funcionario_bp.route('/funcionario/consulta')
def funcionario_consulta():
    funcionarios = Funcionario.CarregarFuncionarios()  # Carrega dados dos funcionários
    return render_template('funcionario_consulta.html', funcionarios=funcionarios)


@funcionario_bp.route('/funcionario/atualizar', methods=['GET', 'POST'])
def usuario_atualizar():
    error_message = ''
    if request.method == 'POST':
        nome = request.form['nome']
        sobrenome = request.form['sobrenome']
        cpf = request.form['cpf']
        rg = request.form['rg']
        email = request.form['email']
        senha = request.form['senha']
        funcionario_loja = True  

        funcionario = Funcionario()
        sucesso = funcionario.Cadastrar_Funcionario({
            'nome': nome,
            'sobrenome': sobrenome,
            'cpf': cpf,
            'rg': rg,
            'email': email,
            'senha': senha,
            'funcionario_loja': funcionario_loja
        })

        error_message = sucesso
        return render_template('funcionario_atualizar.html', error_message=error_message)
    return render_template('funcionario_atualizar.html', error_message=error_message)