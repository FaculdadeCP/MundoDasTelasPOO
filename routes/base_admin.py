from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from routes.home import home_route

administrador = Blueprint('base_admin', __name__) #rota para importar no main

@administrador.route('/admin') #rota do site
def base_admin(): 
    "Administrador" #Aparece como nome da pagina
    return render_template('base_admin.html') #pagina que vai redirecionar
