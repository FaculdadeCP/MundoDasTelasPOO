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
    if 'user_id' in session:
        user_id = session['user_id']
        produtos_carrinho = carrinho.CarregarCarrinho(user_id)
        
        return render_template('carrinho.html', message="",produtos=produtos_carrinho)
    else:
        menssagem = "Por favor, faça o login para ver seu carrinho.", "info"
        return render_template('acesso.login',message=menssagem)

@carrinho_bp.route('/limpar', methods=['POST'])
def limpar():
    if 'user_id' in session:
        user_id = session['user_id']
        resultado = carrinho.LimparCarrinho(user_id)
        if resultado:
            flash('Todos os produtos foram removidos do carrinho.', 'success')
        else:
            flash('Não foi possível limpar o carrinho.', 'error')
    else:
        flash('Você precisa estar logado para realizar esta ação.', 'error')
    return redirect(url_for('carrinho.visualizar'))
