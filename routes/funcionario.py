from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from classes.cls_funcionario import  Funcionario
from classes.cls_cargos import Cargo


funcionario_bp = Blueprint('funcionario', __name__) # Rota para importar no main

@funcionario_bp.route('/funcionario/consulta')
def funcionario_consulta():
    funcionarios = Funcionario.CarregarFuncionarios()  # Carrega dados dos funcionários
    return render_template('funcionario_consulta.html', funcionarios=funcionarios)

@funcionario_bp.route('/funcionario/cadastro', methods=['GET', 'POST'])
def funcionario_cadastro():
    error_message = ''
    if request.method == 'POST':
        nome = request.form['nome']
        sobrenome = request.form['sobrenome']
        cpf = request.form['cpf']
        rg = request.form['rg']
        email = request.form['email']
        senha = request.form['senha']
        funcionario_loja = True  
        cep = request.form['cep']
        logradouro = request.form['logradouro']
        numero = request.form['EnderecoNumero']
        bairro = request.form['bairro']
        complemento = request.form['complemento']
        estado = request.form['estado']
        cidade = request.form['cidade']
        telefone = request.form['telefone']
        cargo_id = int(request.form.get('cargo_id', 0))
        funcionarioAtivo = request.form['funcionarioAtivo']
        tipo_endereco = request.form['tipo_endereco']
        is_comercial = tipo_endereco == 'comercial'  # True se comercial, False caso contrário
        is_residencial = tipo_endereco == 'residencial'  # True se residencial, False caso contrário
        
        print("Cargo ID:", cargo_id)
        print(request.form) 
        funcionario = Funcionario()
        sucesso = funcionario.Cadastrar_Funcionario({
            'nome': nome,
            'sobrenome': sobrenome,
            'cpf': cpf,
            'rg': rg,
            'email': email,
            'senha': senha,
            'funcionario_loja': funcionario_loja,
            'cep': cep,
            'logradouro': logradouro,
            'numero': numero,
            'bairro': bairro,
            'complemento': complemento,
            'estado': estado,
            'cidade': cidade,
            'telefone': telefone,
            'comercial': is_comercial,
            'residencial': is_residencial,
            'cargo': cargo_id,
            'funcionarioAtivo': funcionarioAtivo
        })
        print(f"estou passando o cargo de id = {cargo_id}")

        error_message = sucesso
        return render_template('funcionario_cadastro.html', error_message=error_message)
    else:
         cargos = Cargo.CarregarCargos()
         return render_template('funcionario_cadastro.html', cargos=cargos)

@funcionario_bp.route('/funcionario/editar/<int:id>',methods=['GET', 'POST'])
def funcionario_editar(id):
    
    if request.method == 'POST':
        nome = request.form['nome']
        sobrenome = request.form['sobrenome']
        cpf = request.form['cpf']
        rg = request.form['rg']
        email = request.form['email']
        senha = request.form['senha']
        funcionario_loja = True  
        cep = request.form['cep']
        logradouro = request.form['logradouro']
        numero = request.form['EnderecoNumero']
        bairro = request.form['bairro']
        complemento = request.form['complemento']
        estado = request.form['estado']
        cidade = request.form['cidade']
        telefone = request.form['telefone']
        cargo_id = int(request.form.get('cargo_id', 0))
        funcionarioAtivo = request.form['funcionarioAtivo']
        tipo_endereco = request.form['tipo_endereco']
        is_comercial = tipo_endereco == 'comercial'  # True se comercial, False caso contrário
        is_residencial = tipo_endereco == 'residencial'  # True se residencial, False caso contrário
        pass
    else:
       funcionario = Funcionario.CarregarFuncionario(id)
       print(f"Dados do funcionario: {funcionario}")
       cargos = Cargo.CarregarCargos() 
       return render_template('funcionario_atualizar.html', funcionario=funcionario, cargos=cargos)