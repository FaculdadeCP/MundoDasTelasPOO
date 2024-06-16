from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from routes.home import home_route
from routes.base_admin import administrador
from database.data_access import consultar_usuario
from classes.cls_usuario import Usuario


acesso = Blueprint('acesso', __name__)

@acesso.route('/login', methods=['GET', 'POST'])
def login():
    error_message = ''
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        usuario = consultar_usuario(email=email, senha=password)
        if usuario:
            #dados do usuário:
            session['user_id'] = usuario['id']
            print(f"usuario: {usuario['id']}")
            session['user_email'] = usuario['email']
            session['user_nome'] = usuario['nome']
            session['user_sobrenome'] = usuario['sobrenome']
            session['user_cpfcnpj'] = usuario['cpfcnpj']
            session['user_rg'] = usuario['rg']
            session['user_senha'] = usuario['senha']
            session['logged_in'] = True
            session['funcionarioloja'] = usuario['funcionarioloja']
            #Dados de endereço:
            session['user_cep'] = usuario['cep']
            session['user_logradouro'] = usuario['logradouro']
            session['user_bairro'] = usuario['bairro']
            session['user_complemento'] = usuario['complemento']
            session['user_estado'] = usuario['estado']
            session['user_cidade'] = usuario['cidade']
            session['user_telefone'] = usuario['telefone']
            session['user_numero'] = usuario['numero']
            session['user_residencial'] = usuario['residencial']
            session['user_comercial'] = usuario['comercial']
            if usuario['funcionarioloja']:
                return redirect(url_for('base_admin.base_admin'))  # Redireciona para a tela do administrador
            else:
                return redirect(url_for('home.home'))  # Redireciona para a tela padrão
        else:
            error_message = 'Usuário ou senha incorretos!'
            return render_template('login.html', message=error_message)
    return render_template('login.html', error_message=error_message)

@acesso.route('/logout')
def logout():
    session.pop('user_id', None)
    session.pop('user_email', None)
    session.pop('logged_in', None)
    session.pop('funcionarioloja', None)
    return redirect(url_for('acesso.login'))

@acesso.route('/usuario_cadastro', methods=['GET', 'POST'])
def usuario_cadastro():
    error_message = ''
    if request.method == 'POST':
        nome = request.form['nome']
        sobrenome = request.form['sobrenome']
        cpf = request.form['cpf']
        rg = request.form['rg']
        email = request.form['email']
        senha = request.form['senha']
        funcionario_loja = False  

        usuario = Usuario()
        sucesso = usuario.cadastrar_usuario({
            'nome': nome,
            'sobrenome': sobrenome,
            'cpf': cpf,
            'rg': rg,
            'email': email,
            'senha': senha,
            'funcionario_loja': funcionario_loja
        })

        error_message = sucesso
        return render_template('usuario_cadastro.html', error_message=error_message)
    return render_template('usuario_cadastro.html', error_message=error_message)
       
