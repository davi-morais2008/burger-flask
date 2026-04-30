from flask import Flask, render_template, redirect, request, session, flash, jsonify
from model.produto import recuperar_produtos
from model.usuario import cadastrar, login
from model.carrinho import recuperar_carrinho


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
        flash("Usuário já existe.", "danger")
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
        flash("Usuário ou senha incorretos.", "danger")
        return redirect("/login")
    
@app.route("/logout")
def deslogar():
    session.clear()
    return redirect("/")


@app.route("/api/get/carrinho")
def api_get_carrinho():
    if "usuario_logado" in session:
        carrinho = recuperar_carrinho(session["usuario_logado"])
        return jsonify(carrinho), 200
    else:
        return jsonify({"message": "Usuário não logado"}), 401

app.run(host='0.0.0.0', port=8080, debug=True)