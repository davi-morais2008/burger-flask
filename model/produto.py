from database.conexao import conectar

def recuperar_produtos():
    conexao, cursor = conectar()
    cursor.execute("SELECT codigo, produto, descricao, preco, destaque, foto, disponibilidade FROM burguer")
    produto = cursor.fetchall()
    conexao.close()

    return produto