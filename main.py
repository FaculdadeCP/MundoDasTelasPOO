# main.py
from flask import Flask
from database.database import db
from routes.home import home_route
from routes.acesso import acesso
from routes.produto import produto_bp
from routes.base_admin import administrador

#Rota para apagar de TESTE
from routes.TESTE import teste

app = Flask(__name__)
app.secret_key = 'm0nd0d4st3l4s'

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://xelfcdut:2DHCHniJlOswtUcXjf0CuPlkZJUy3Zri@kesavan.db.elephantsql.com/xelfcdut'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

app.register_blueprint(home_route)
app.register_blueprint(acesso, url_prefix='')
app.register_blueprint(produto_bp, url_prefix='/produtos')
app.register_blueprint(administrador, url_prefix='')
app.register_blueprint(teste, url_prefix='')

if __name__ == '__main__':
    app.run(debug=True)
