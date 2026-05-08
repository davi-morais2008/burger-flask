const carrinhoLateral = document.getElementById('shopping-cart');
const btnFechar = document.getElementById('close-cart');
const btnAbrir = document.getElementById('cart');

// Função para abrir
btnAbrir.addEventListener('click', () => {
    carrinhoLateral.classList.add('carrinho-aberto');
});

// Função para fechar
btnFechar.addEventListener('click', () => {
    carrinhoLateral.classList.remove('carrinho-aberto');
});

async function carregarCarrinho() {
    const resposta = await fetch("http://127.0.0.1:8080/api/get/carrinho")

    if (!resposta.ok){
        alert("ERRO AO CARREGAR CARRINHO!")
    }
    else{
        const dados = await resposta.json()

        const banner = document.getElementById('carrinho')
        const p = document.querySelector('.cart-total__value')

        banner.innerHTML = ''

        let precoTotal = 0

        for (let dado of dados){
            let linha =  `
            <div class="cart-item">
                <div class="cart-item__info">
                    <p class="cart-item__name">${dado.produto}</p>
                    <p class="cart-item__price">R$ ${dado.preco}</p>
                    <p class="cart-item__price">Quantidade: ${dado.quantidade}</p>
                </div>
                <button class="cart-item__remove">Remover</button>
            </div>
            `
            banner.innerHTML += linha
            precoTotal += dado.preco
        }
        p.textContent = 'R$ ' + precoTotal
    }   
}


async function inserirItemCarrinho(cod_produto, quantidade=1) {
    const resposta = await fetch("/api/post/carrinho", {
                                                            method:"POST", 
                                                            headers: {"Content-Type": "application/json"}, 
                                                            body: JSON.stringify(
                                                                                    {
                                                                                        "codigo": cod_produto,
                                                                                        "quantidade": quantidade
                                                                                    }
                                                            )
                                                        }
                                                    )
    if(!resposta.ok){
        alert("Erroooo")
    }
    carregarCarrinho();

}

carregarCarrinho()


