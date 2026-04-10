from flask import Flask, render_template
from model.produto import recuperar_produtos

app = Flask(__name__)

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

app.run(host='0.0.0.0', port=8080, debug=True)