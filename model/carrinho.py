from database.conexao import conectar
import mysql.connector

def recuperar_carrinho(usuario):
    conexao, cursor = conectar()
    cursor.execute("""
                    SELECT burguer.produto, carrinho.codigo, usuario.username, carrinho.finalizado, itens_carrinho.quantidade, burguer.preco, burguer.foto FROM carrinho
                    INNER JOIN itens_carrinho ON carrinho.codigo = itens_carrinho.cod_carrinho
                    INNER JOIN burguer ON burguer.codigo = itens_carrinho.cod_burguer
                    INNER JOIN usuario ON usuario.username = carrinho.usuario
                    WHERE carrinho.usuario = %s""", (usuario,))
    carrinho = cursor.fetchall()
    conexao.commit()
    conexao.close()

    return carrinho


def add_item(usuario, cod_item, quantidade=1):
    conexao, cursor = conectar()
    cursor.execute("SELECT codigo FROM carrinho WHERE usuario = %s AND finalizado = 0 limit 1", (usuario,))
    resultado_carrinho = cursor.fetchone()

    if resultado_carrinho:
        codigo_carrinho = resultado_carrinho["codigo"]
    else:
        cursor.execute("INSERT INTO carrinho (usuario) VALUES (%s);", (usuario,))
        codigo_carrinho = cursor.lastrowid

        cursor.execute("INSERT INTO itens_carrinho (cod_carrinho, cod_burguer, quantidade) VALUES (%s, %s, %s)", (codigo_carrinho, cod_item, quantidade))

    conexao.commit()
    conexao.close()