from database.database import db
from datetime import datetime
class Pessoa(db.Model):
    __tablename__ = 'tb_pessoas'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(250))
    sobrenome = db.Column(db.String(250))
    cpfcnpj = db.Column(db.String(20))
    rg = db.Column(db.String(16))
    email = db.Column(db.String(250))
    senha = db.Column(db.String(250))
    pj = db.Column(db.Boolean)
    funcionarioloja = db.Column(db.Boolean)
    enderecos = db.relationship('ListaEnderecos', backref='pessoa')

class Endereco(db.Model):
    __tablename__ = 'tb_enderecos'
    id = db.Column(db.Integer, primary_key=True)
    cep = db.Column(db.String(10))
    logradouro = db.Column(db.String(250))
    numero = db.Column(db.Integer)
    bairro = db.Column(db.String(250))
    complemento = db.Column(db.String(250))
    estado = db.Column(db.String(2))
    cidade = db.Column(db.String(250))
    telefone = db.Column(db.String(14))
    listaEnderecos = db.relationship('ListaEnderecos', backref='endereco')

class ListaEnderecos(db.Model):
    __tablename__ = 'tb_listaenderecos'
    pessoas_id = db.Column(db.Integer, db.ForeignKey('tb_pessoas.id'), primary_key=True)
    enderecos_id = db.Column(db.Integer, db.ForeignKey('tb_enderecos.id'), primary_key=True)
    nomeEndereco = db.Column(db.String(250))

class Fornecedor(db.Model):
    __tablename__ = 'tb_fornecedores'
    id = db.Column(db.Integer, primary_key=True)
    enderecos_id = db.Column(db.Integer, db.ForeignKey('tb_enderecos.id'))
    nome_empresa = db.Column(db.String(250))
    representante = db.Column(db.String(250))
    telefone_representante = db.Column(db.String(14))
    cnpj = db.Column(db.String(20))
    endereco = db.relationship('Endereco', backref='fornecedores')

class Status(db.Model):
    __tablename__ = 'tb_status'
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.String(50))

class Pedido(db.Model):
    __tablename__ = 'tb_pedidos'
    id = db.Column(db.Integer, primary_key=True)
    pessoas_id = db.Column(db.Integer, db.ForeignKey('tb_pessoas.id'))
    status_id = db.Column(db.Integer, db.ForeignKey('tb_status.id'))
    datahora_pedido = db.Column(db.Date)
    pessoa = db.relationship('Pessoa', backref='pedidos')
    status = db.relationship('Status', backref='pedidos')

class FormaPagamento(db.Model):
    __tablename__ = 'tb_formaspagamentos'
    id = db.Column(db.Integer, primary_key=True)
    forma_pagamento = db.Column(db.String(50))
    permite_parcela = db.Column(db.Boolean)

class PedidoCobranca(db.Model):
    __tablename__ = 'tb_pedidoscobrancas'
    id = db.Column(db.Integer, primary_key=True)
    pedidos_id = db.Column(db.Integer, db.ForeignKey('tb_pedidos.id'))
    formas_pagamentos_id = db.Column(db.Integer, db.ForeignKey('tb_formaspagamentos.id'))
    tem_parcela = db.Column(db.Boolean)
    data_cobranca_parcela = db.Column(db.Date)
    quantidade_parcela = db.Column(db.Integer)
    valor_parcela = db.Column(db.Numeric)
    valor_frete = db.Column(db.Numeric)
    valor_total_pedido = db.Column(db.Numeric)
    pedido = db.relationship('Pedido', backref='cobrancas')
    forma_pagamento = db.relationship('FormaPagamento', backref='cobrancas')

class Produto(db.Model):
    __tablename__ = 'tb_produtos'
    id = db.Column(db.Integer, primary_key=True)
    marca = db.Column(db.String(250))
    modelo = db.Column(db.String(250))
    tamanho_tela = db.Column(db.Float)
    tipo_iluminacao = db.Column(db.String(20))
    proporcao = db.Column(db.String(20))
    taxa_contraste = db.Column(db.String(20))
    tempo_resposta = db.Column(db.String(20))
    interfase_saida = db.Column(db.String(20))
    cor = db.Column(db.String(20))
    brilho = db.Column(db.String(20))
    resolucao_maxima = db.Column(db.String(20))
    taxa_atualizacao = db.Column(db.String(20))
    descricao = db.Column(db.String(250))
    caminho_imagem = db.Column(db.String(250))
    valor = db.Column(db.Numeric)
    monitor = db.Column(db.Boolean)
    estoques = db.relationship('Estoque', backref='produto')

class Estoque(db.Model):
    __tablename__ = 'tb_estoque'
    produtos_id = db.Column(db.Integer, db.ForeignKey('tb_produtos.id'), primary_key=True)
    fornecedores_id = db.Column(db.Integer, db.ForeignKey('tb_fornecedores.id'), primary_key=True)
    quantidade = db.Column(db.Integer)
    data_entrada = db.Column(db.Date)
    data_saida = db.Column(db.Date)
    fornecedor = db.relationship('Fornecedor', backref='estoque')
