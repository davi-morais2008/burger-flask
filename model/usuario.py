from database.conexao import conectar
import mysql.connector

def cadastrar(usuario, senha):
    conexao, cursor = conectar()
    