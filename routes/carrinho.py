from flask import Blueprint, render_template, request, session, redirect, url_for, flash
from classes.cls_carrinho import carrinho

carrinho_bp = Blueprint('carrinho', __name__)

@carrinho_bp.route('/adicionar', methods=['POST'])
def adicionar():
    if 'user_id' in session:
        user_id = session['user_id']
        print(f"usuario: {user_id}")
        product_id = request.form.get('product_id')
        print(f"produto: {product_id}")
        quantidade = request.form.get('quantity', type=int, default=1)
        result = carrinho.AdicionarProduto(user_id, product_id, quantidade)
        if result == "Ocorreu um erro!":
            return redirect(url_for('home.home',message="Ocorreu um erro ao tentar adicionar o produto!, tente novamente mais tarde"))
        return redirect(url_for('carrinho.visualizar'))  # Redireciona para a página do carrinho após adicionar
    else:
        message = "Usuário não identificado, por gentileza faça o Login!"
        return render_template('login.html',message=message)

@carrinho_bp.route('/visualizar',methods=['POST','GET'])
def visualizar():
     if request.method == 'POST':
         return render_template('carrinho.html')
     else: 
         return render_template('carrinho.html')