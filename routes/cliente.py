from flask import Blueprint

cliente_route = Blueprint('cliente', __name__)

"""
Rota de Clientes

    - /clientes/                Listar clientes                                     (get)
    - /clientes/new             inserir novo cliente no servidor                    (post)               
     - /clientes/new            renderizar um formulario para criar um cliente      (get)
    - /clientes/<id>            obter os dados de um cliente                        (get)
    - /clientes/<id>/edit       renderizar um formulario para editar um cliente     (get)
    - /clientes/<id>/update     atualizar os dados do cliente                       (put)
    - /clientes/<id>/delete     deleta registro do usuario                          (delete)

"""


@cliente_route.route('/')
def lista_clientes():
    pass

@cliente_route.route('/<int:cliente_id>')
def obter_cliente(cliente_id):
    pass