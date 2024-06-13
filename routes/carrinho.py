from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from routes.home import home_route

carrinho_bp = Blueprint('carrinho', __name__) #rota para importar no main

@carrinho_bp.route('/carrinho') #rota do site
def carrinho(): 
    "carrinho" #Aparece como nome da pagina
    return render_template('carrinho.html') #pagina que vai redirecionar
