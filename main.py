from flask import Flask
#importando rota
from routes.home import home_route


#inicializacao
app = Flask(__name__)

app.register_blueprint(home_route)

#execucao
app.run(debug=True)