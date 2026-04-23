async function mostrarCarrinho() {
    const resposta = await fetch("http://10.110.134.2:8080/api/get/carrinho")

    if (!resposta.ok){
        alert('ERRO AO CARREGAR CARRINHO!')
    } else {
        const dados = await resposta.json()

        const carrinho = document.getElementById('carrinho')

        carrinho.innerHTML = '';

        for (let dado of dados){
            let linha = `
            <div class="cart-item" >
                <div class="cart-item__info" >
                    <p class="cart-item__name">${dado.nome}</p>
                    <p class="cart-item__price">${dado.preco}</p>
                </div>
                <span class="material-symbols-outlined">
                    delete
                </span>
            </div>
            `
            carrinho.innerHTML += linha
        }
    }
}

mostrarCarrinho();