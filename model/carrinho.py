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