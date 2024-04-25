from flask import Flask,url_for, render_template

#inicializacao
app = Flask(__name__)

#rotas
@app.route('/')
def ola_mundo():
    titulo = "Gestão de usuários"
    usuarios = [
        {"nome": "Guilherme","Membro_ativo": True},
        {"nome": "João","Membro_ativo": False},
        {"nome": "Maria","Membro_ativo": True},
    ]
    return render_template("index.html",titulo=titulo, usuarios=usuarios)

@app.route('/sobre')
def pagina_sobre():
    return "aaaaaa ?"

#execucao
app.run(debug=True)


