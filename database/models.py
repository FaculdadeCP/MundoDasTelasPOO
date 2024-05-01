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