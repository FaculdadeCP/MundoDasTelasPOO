from flask import Blueprint, render_template, request, redirect, url_for, session, flash

teste = Blueprint('base_admin_teste', __name__) #rota para importar no main

@teste.route('/teste') #rota do site
def base_teste(): 
    "teste" #Aparece como nome da pagina
    return render_template('base_admin_teste.html') #pagina que vai redirecionar
