const carrinho = document.getElementById('shopping-cart');
const btnFechar = document.getElementById('close-cart');
const btnAbrir = document.getElementById('cart');

// Função para abrir
btnAbrir.addEventListener('click', () => {
    carrinho.classList.add('carrinho-aberto');
});

// Função para fechar
btnFechar.addEventListener('click', () => {
    carrinho.classList.remove('carrinho-aberto');
});

async function  carregarCarrinho() {
    const resposta = await fetch("http://10.110.134.2:8080/api/get/carrinho")

    if (!resposta.ok){
        alert("ERRO AO CARREGAR CARRINHO!")
    }
    else{
        const dados = await resposta.json()

        console.log(dados
        )

        const carrinho = document.getElementById('carrinho')
        const p = document.querySelector('.cart-total__value')

        carrinho.innerHTML = ''

        let precoTotal = 0

        for (let dado of dados){
            let linha =  `
            <div class="cart-item">
                <div class="cart-item__info">
                    <p class="cart-item__name">${dado.nome}</p>
                    <p class="cart-item__price">R$ ${dado.preco}</p>
                </div>
                <button class="cart-item__remove">Remover</button>
            </div>
            `
            carrinho.innerHTML += linha
            precoTotal += dado.preco
        }
        p.textContent = 'R$ ' + precoTotal
    }   
}

carregarCarrinho()