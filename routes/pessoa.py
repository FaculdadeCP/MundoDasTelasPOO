# routes/pessoa.py
from flask import Blueprint, render_template, request
from database.database import db
from database.data_access import consultar_pessoa_por_nome

pessoa_bp = Blueprint('pessoa', __name__, template_folder='../templates')
pessoa_pesquisa = Blueprint('pesquisa Pessoa',__name__,template_folder='../templates')

@pessoa_bp.route('/pesquisar_cliente', methods=['GET'])

def pesquisar_cliente():
    nome = request.args.get('nome')
    pessoa = consultar_pessoa_por_nome(nome)
    if pessoa:
        print(f"Pessoa encontrada: {pessoa['nome']}")  # Agora você pode acessar por nome de coluna
        print(pessoa)
        return render_template('exibe_cliente.html', pessoa=pessoa)
    else:
        return 'Cliente não encontrado', 404

@pessoa_pesquisa.route('/formulario_pesquisa')
def formulario_pesquisa():
    return render_template('pesquisa_cliente.html')