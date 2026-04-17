from flask import Flask, render_template, redirect, request, session
from model.produto import recuperar_produtos
from model.usuario import cadastrar, login

app = Flask(__name__)

app.secret_key = 'megamats'

@app.route("/")
def page_home():
    produtos = recuperar_produtos()
    return render_template("index.html", produtos = produtos)

@app.route("/pagina")
def page_2():
    return render_template("produto.html")

@app.route("/produto/<id>")
def page_product(id):
    produto = recuperar_produtos(id)
    return render_template("produto.html", produto = produto)

@app.route("/cadastro")
def page_signup():
    return render_template("cadastro.html")


@app.route("/cadastro/send", methods=["POST"])
def cadastro_post():
    user = request.form.get("nome")
    senha = request.form.get("senha")
    
    if cadastrar(user, senha):
        session['usuario_logado'] = user
        return redirect("/")
    else:
        return redirect("/cadastro")
    
@app.route("/login")
def page_login():
    return render_template("login.html")

@app.route("/login/send", methods=["POST"])
def login_post():
    user = request.form.get("nome")
    senha = request.form.get("senha")
    
    if login(user, senha):
        session['usuario_logado'] = user
        return redirect("/")
    else:
        return redirect("/login")
    
@app.route("/logout")
def deslogar():
    session.clear()
    return redirect("/")

app.run(host='0.0.0.0', port=8080, debug=True)