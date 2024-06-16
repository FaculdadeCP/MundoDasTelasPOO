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
            flash("Erro ao adicionar produto ao carrinho", "error")  # Use flash para enviar mensagens de erro ou sucesso.
            return redirect(url_for('home.home'))
        return redirect(url_for('home.home'))  # Redireciona para a página do carrinho após adicionar
    else:
        flash("Usuário não identificado", "error")
        return redirect(url_for('acesso.login'))  # Supondo que você tenha uma rota de login

@carrinho_bp.route('/carrinho',methods=['GET'])
def visualizar():
    return render_template('carrinho.html')