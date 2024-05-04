from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from routes.home import home_route
from database.data_access import consultar_usuario

acesso = Blueprint('acesso', __name__)

@acesso.route('/login', methods=['GET', 'POST'])
def login():
    error_message = ''
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        if consultar_usuario(email=email, senha=password):
            return redirect(url_for('home.home'))
        else:
            error_message = 'Usuário ou senha incorretos!'
            return render_template('login.html', error_message=error_message)
    return render_template('login.html', error_message=error_message)

@acesso.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect(url_for('acesso.login'))

