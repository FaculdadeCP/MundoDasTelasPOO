#importando Bibliotecas
from flask import Flask
from database.database import db
from routes.pessoa import pessoa_bp, pessoa_pesquisa

#importando rota
from routes.home import home_route
from routes.cliente import cliente_route


#inicializacao
app = Flask(__name__)

# Configurações do banco de dados
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://xelfcdut:2DHCHniJlOswtUcXjf0CuPlkZJUy3Zri@kesavan.db.elephantsql.com/xelfcdut'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicialização do objeto SQLAlchemy
db.init_app(app)

# Definindo Rotas
app.register_blueprint(home_route)
app.register_blueprint(cliente_route, url_prefix='/clientes')
app.register_blueprint(pessoa_bp)
app.register_blueprint(pessoa_pesquisa)


#execucao

app.run(debug=True)


