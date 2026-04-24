from database.conexao import conectar
import mysql.connector

def recuperar_carrinho(usuario):
    conexao, cursor = conectar()
    cursor.execute("SELECT codigo, username, finalizado FROM carrinho WHERE username = %s", (usuario,))
    carrinho = cursor.fetchall()
    conexao.commit()
    conexao.close()

    return carrinho