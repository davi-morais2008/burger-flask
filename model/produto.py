from database.conexao import conectar

def recuperar_produtos(id=False):
    conexao, cursor = conectar()
    if id:
        cursor.execute("SELECT codigo, produto, descricao, preco, destaque, foto, disponibilidade FROM burguer WHERE codigo = %s", (id,))
        produto = cursor.fetchone()
    else:
        cursor.execute("SELECT codigo, produto, descricao, preco, destaque, foto, disponibilidade FROM burguer")
        produto = cursor.fetchall()
    conexao.close()

    return produto