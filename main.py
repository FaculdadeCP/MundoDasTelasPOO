from flask import Flask
#importando rota
from routes.home import home_route
from routes.cliente import cliente_route


#inicializacao
app = Flask(__name__)

app.register_blueprint(home_route)
app.register_blueprint(cliente_route, url_prefix='/clientes')

#execucao

app.run(debug=True)


