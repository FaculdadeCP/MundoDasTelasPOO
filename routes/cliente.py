from flask import Blueprint, render_template
from database.cliente import CLIENTES
from database.models import Pessoa 

cliente_route = Blueprint('cliente', __name__)


@cliente_route.route('/')
def lista_clientes():
    """Listar os clientes"""
    return render_template('lista_clientes.html', cleintes=CLIENTES)


@cliente_route.route('/', methods=['POST'])
def inserir_cliente():
    """Inserir dados dos clientes"""
    pass


@cliente_route.route('/new')
def form_cliente ():
    """formulario para cadastrar um cliente"""
    return render_template('form_cliente.html')



@cliente_route.route('/cliente/<int:id>')
def detalhe_cliente(id):
    cliente = Pessoa.query.get_or_404(id)
    return render_template('detalhe_cliente.html', cliente=cliente)



@cliente_route.route('/<int:cliente_id>/edit')
def form_edit_cliente (cliente_id):
    """ formulario para editar um cliente """
    return render_template('form_edit_cliente.html')


@cliente_route.route('/<int:cliente_id>/update', methods=['PUT'])
def atualizar_cliente (cliente_id):
    """Atualizar informações do cliente"""
    pass


@cliente_route.route('/<int:cliente_id>/delete', methods=['DELETE'])
def deletar_cliente (cliente_id):
    """ deletar informacoes do cliente"""
    pass

