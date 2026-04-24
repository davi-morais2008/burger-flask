SELECT carrinho.codigo, usuario.username, carrinho.finalizado, itens_carrinho.quantidade, burguer.preco, burguer.foto FROM carrinho
INNER JOIN itens_carrinho ON carrinho.codigo = itens_carrinho.cod_carrinho
INNER JOIN burguer ON burguer.codigo = itens_carrinho.cod_burguer