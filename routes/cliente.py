from flask import Blueprint

cliente_route = Blueprint('cliente', __name__)

"""
Rota de Clientes

    - /clientes/                
     - /clientes/new            renderizar um formulario para criar um cliente      (get)
    - /clientes/new             inserir novo cliente no servidor                    (post)
    - /clientes/<id>            obter os dados de um cliente                        (get)
    - /clientes/<id>/edit       renderizar um formulario para editar um cliente     (get)
    - /clientes/<id>/update     atualizar os dados do cliente                       (put)
    - /clientes/<id>/delete     deleta registro do usuario                          (delete)

    16:09
"""


@cliente_route.route('/')
def lista_clientes():
    pass

@cliente_route.route('/<int:cliente_id>')
def obter_cliente(cliente_id):
    pass