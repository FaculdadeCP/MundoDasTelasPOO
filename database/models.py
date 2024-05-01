from database import db
from datetime import datetime

# Modelo para Pessoas
class Pessoa(db.Model):
    __tablename__ = 'tb_Pessoas'
    id = db.Column(db.Integer, primary_key=True)
    Nome = db.Column(db.String(250))
    Sobrenome = db.Column(db.String(250))
    CpfCnpj = db.Column(db.String(20))
    RG = db.Column(db.String(16))
    Email = db.Column(db.String(250))
    Senha = db.Column(db.String(250))
    PJ = db.Column(db.Boolean)

# Modelo para Endereços
class Endereco(db.Model):
    __tablename__ = 'tb_Enderecos'
    id = db.Column(db.Integer, primary_key=True)
    CEP = db.Column(db.String(10))
    Logradouro = db.Column(db.String(250))
    Numero = db.Column(db.Integer)
    Bairro = db.Column(db.String(250))
    Complemento = db.Column(db.String(250))
    Estado = db.Column(db.String(2))
    Cidade = db.Column(db.String(250))
    Telefone = db.Column(db.String(14))

# Modelo para Lista de Endereços
class ListaEnderecos(db.Model):
    __tablename__ = 'tb_ListaEnderecos'
    Pessoas_id = db.Column(db.Integer, db.ForeignKey('tb_Pessoas.id'), primary_key=True)
    Enderecos_id = db.Column(db.Integer, db.ForeignKey('tb_Enderecos.id'), primary_key=True)
    NomeEndereco = db.Column(db.String(250))
    pessoa = db.relationship('Pessoa', backref='lista_enderecos')
    endereco = db.relationship('Endereco', backref='lista_enderecos')

# Modelo para Fornecedores
class Fornecedor(db.Model):
    __tablename__ = 'tb_Fornecedores'
    id = db.Column(db.Integer, primary_key=True)
    Enderecos_id = db.Column(db.Integer, db.ForeignKey('tb_Enderecos.id'))
    nomeEmpresa = db.Column(db.String(250))
    representante = db.Column(db.String(250))
    telefoneRepresentante = db.Column(db.String(14))
    CNPJ = db.Column(db.String(20))
    endereco = db.relationship('Endereco', backref='fornecedores')

# Modelo para Status
class Status(db.Model):
    __tablename__ = 'tb_Status'
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.String(50))

# Modelo para Pedidos
class Pedido(db.Model):
    __tablename__ = 'tb_Pedidos'
    id = db.Column(db.Integer, primary_key=True)
    Pessoas_id = db.Column(db.Integer, db.ForeignKey('tb_Pessoas.id'))
    Status_id = db.Column(db.Integer, db.ForeignKey('tb_Status.id'))
    datahoraPedido = db.Column(db.Date)
    pessoa = db.relationship('Pessoa', backref='pedidos')
    status = db.relationship('Status', backref='pedidos')

# Modelo para Formas de Pagamento
class FormaPagamento(db.Model):
    __tablename__ = 'tb_FormasPagamentos'
    id = db.Column(db.Integer, primary_key=True)
    formaPagamento = db.Column(db.String(50))
    permiteParcela = db.Column(db.Boolean)

# Modelo para Pedidos Cobranças
class PedidoCobranca(db.Model):
    __tablename__ = 'tb_PedidosCobrancas'
    id = db.Column(db.Integer, primary_key=True)
    Pedidos_id = db.Column(db.Integer, db.ForeignKey('tb_Pedidos.id'))
    FormasPagamentos_id = db.Column(db.Integer, db.ForeignKey('tb_FormasPagamentos.id'))
    temParcela = db.Column(db.Boolean)
    DataCobrancaParcela = db.Column(db.Date)
    quantiadeParcela = db.Column(db.Integer)
    valorParcela = db.Column(db.Numeric)
    ValorFrete = db.Column(db.Numeric)
    valorTotalPedido = db.Column(db.Numeric)
    pedido = db.relationship('Pedido', backref='cobrancas')
    forma_pagamento = db.relationship('FormaPagamento', backref='cobrancas')

# Modelo para Produtos
class Produto(db.Model):
    __tablename__ = 'tb_Produtos'
    id = db.Column(db.Integer, primary_key=True)
    Marca = db.Column(db.String(250))
    Modelo = db.Column(db.String(250))
    TamanhoTela = db.Column(db.Float)
    tipoIluminacao = db.Column(db.String(20))
    Proporcao = db.Column(db.String(20))
    taxaContraste = db.Column(db.String(20))
    tempoResposta = db.Column(db.String(20))
    interfaseSaida = db.Column(db.String(20))
    Cor = db.Column(db.String(20))
    Brilho = db.Column(db.String(20))
    ResolucaoMaxima = db.Column(db.String(20))
    TaxaAtualizacao = db.Column(db.String(20))
    Descricao = db.Column(db.String(250))
    CaminhoImagem = db.Column(db.String(250))
    Valor = db.Column(db.Numeric)
    monitor = db.Column(db.Boolean)

# Modelo para Pedidos Itens
class PedidoItem(db.Model):
    __tablename__ = 'tb_PedidosItens'
    Pedidos_id = db.Column(db.Integer, db.ForeignKey('tb_Pedidos.id'), primary_key=True)
    Produtos_id = db.Column(db.Integer, db.ForeignKey('tb_Produtos.id'), primary_key=True)
    quantidade = db.Column(db.Integer)
    valorItem = db.Column(db.Numeric)
    descontoItem = db.Column(db.Float)
    freteItem = db.Column(db.Float)
    pedido = db.relationship('Pedido', backref='itens')
    produto = db.relationship('Produto', backref='itens')

# Modelo para Estoque
class Estoque(db.Model):
    __tablename__ = 'tb_Estoque'
    Produtos_id = db.Column(db.Integer, db.ForeignKey('tb_Produtos.id'), primary_key=True)
    fornecedores_id = db.Column(db.Integer, db.ForeignKey('tb_Fornecedores.id'), primary_key=True)
    quantidade = db.Column(db.Integer)
    dataEntrada = db.Column(db.Date)
    dataSaida = db.Column(db.Date)
    produto = db.relationship('Produto', backref='estoque')
    fornecedor = db.relationship('Fornecedor', backref='estoque')
