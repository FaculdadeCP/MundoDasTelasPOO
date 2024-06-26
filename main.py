# main.py
from flask import Flask
from database.database import db
from routes.home import home_route
from routes.acesso import acesso
from routes.base_admin import administrador
from routes.perfil import perfil_bp
from routes.produto import produto_bp
from routes.fornecedor import fornecedor_cadastro_bp
from routes.funcionario import funcionario_bp
from routes.carrinho import carrinho_bp

# Rota para apagar de TESTE
from routes.TESTE import teste

app = Flask(__name__)
app.secret_key = 'm0nd0d4st3l4s'

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://xelfcdut:2DHCHniJlOswtUcXjf0CuPlkZJUy3Zri@kesavan.db.elephantsql.com/xelfcdut'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

@app.template_filter('currency_format')
def currency_format(value):
    return f"{value:,.2f}"


db.init_app(app)

app.register_blueprint(home_route)
app.register_blueprint(acesso, url_prefix='')
app.register_blueprint(administrador, url_prefix='')
app.register_blueprint(perfil_bp, url_prefix='')
app.register_blueprint(produto_bp, url_prefix='')
app.register_blueprint(teste, url_prefix='')
app.register_blueprint(fornecedor_cadastro_bp, url_prefix='')
app.register_blueprint(funcionario_bp, url_prefix='')
app.register_blueprint(carrinho_bp,url_prefix='')

if __name__ == '__main__':
    app.run(debug=True) 
