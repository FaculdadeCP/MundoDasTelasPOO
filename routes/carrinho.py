from flask import Blueprint, render_template, request, session,redirect,url_for
from classes.cls_produto import Produto

carrinho_bp = Blueprint('carrinho', __name__)

def adicionar_ao_carrinho(produto_id, quantidade):
    if 'carrinho' not in session:
        session['carrinho'] = {}
    
    if produto_id in session['carrinho']:
        session['carrinho'][produto_id] += quantidade  # Incrementa a quantidade
    else:
        session['carrinho'][produto_id] = quantidade  # Adiciona novo produto com sua quantidade
    
    session.modified = True  # Garante que a sessão foi modificada


@carrinho_bp.route('/carrinho', methods=['GET'])
def carrinho():
    produtos_carrinho = []
    if 'carrinho' in session:
        for produto_id, quantidade in session['carrinho'].items():
            produto = Produto.consultar_produto(produto_id)
            if produto:
                produto_info = {
                    'detalhes': produto,
                    'quantidade': quantidade
                }
                produtos_carrinho.append(produto_info)
    
    return render_template('carrinho.html', produtos=produtos_carrinho)
@carrinho_bp.route('/carrinho/formaPagmaento',methods=['GET'])
def forma_pagamento():
    return render_template('carrinho_forma_pagamento.html') # Página que vai redirecionar