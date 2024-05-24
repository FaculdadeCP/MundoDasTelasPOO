# main.py
from flask import Flask
from database.database import db
from routes.pessoa import pessoa_bp, pessoa_pesquisa
from routes.home import home_route
from routes.cliente import cliente_route
from routes.acesso import acesso
from routes.produto import produto_bp

app = Flask(__name__)
app.secret_key = 'm0nd0d4st3l4s'

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://xelfcdut:2DHCHniJlOswtUcXjf0CuPlkZJUy3Zri@kesavan.db.elephantsql.com/xelfcdut'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

app.register_blueprint(home_route)
app.register_blueprint(cliente_route, url_prefix='/clientes')
app.register_blueprint(pessoa_bp, url_prefix='/pessoas')
app.register_blueprint(pessoa_pesquisa, url_prefix='/pessoas')
app.register_blueprint(acesso, url_prefix='/acesso')
app.register_blueprint(produto_bp, url_prefix='/produtos')

if __name__ == '__main__':
    app.run(debug=True)
