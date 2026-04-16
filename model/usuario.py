from database.conexao import conectar
import mysql.connector

def cadastrar(user, senha):
    conexao, cursor = conectar()
    
    try:
        cursor.execute("INSERT INTO usuario(username, senha) VALUES (%s, %s)", (user, senha))
        conexao.commit()
        conexao.close()
        return True
    except:
        return False
    
def login(user, senha):
    conexao, cursor = conectar()
    cursor.execute("SELECT username, senha FROM usuario WHERE username = %s", (user,))
    resultado = cursor.fetchone()

    if resultado['senha']  == senha:
        return True
    
    return False