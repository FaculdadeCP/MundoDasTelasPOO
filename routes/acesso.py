from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from routes.home import home_route
from routes.base_admin import administrador
from database.data_access import consultar_usuario

acesso = Blueprint('acesso', __name__)

@acesso.route('/login', methods=['GET', 'POST'])
def login():
    error_message = ''
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        usuario = consultar_usuario(email=email, senha=password)
        if usuario:
            session['user_id'] = usuario['id']
            session['user_email'] = usuario['email']
            session['logged_in'] = True
            session['funcionarioloja'] = usuario['funcionarioloja']
            if usuario['funcionarioloja']:
                return redirect(url_for('base_admin.base_admin'))  # Redireciona para a tela do administrador
            else:
                return redirect(url_for('home.home'))  # Redireciona para a tela padrão
        else:
            error_message = 'Usuário ou senha incorretos!'
            return render_template('login.html', error_message=error_message)
    return render_template('login.html', error_message=error_message)

@acesso.route('/logout')
def logout():
    session.pop('user_id', None)
    session.pop('user_email', None)
    session.pop('logged_in', None)
    session.pop('funcionarioloja', None)
    return redirect(url_for('acesso.login'))

@acesso.route('/usuario_cadastro')
def usuario_cadastro():
    session.clear()  # Limpa a sessão antes de acessar a página de cadastro
    return render_template('usuario_cadastro.html')