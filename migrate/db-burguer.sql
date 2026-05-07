CREATE DATABASE IF NOT EXISTS db_burguers;
USE db_burguers;

CREATE TABLE IF NOT EXISTS burguer(
    codigo INT PRIMARY KEY AUTO_INCREMENT,
    produto VARCHAR(50),
    descricao VARCHAR(100),
    preco DOUBLE(7,2),
    destaque BOOL DEFAULT 0,
    foto VARCHAR(200),
    disponibilidade BOOL DEFAULT 1
);

CREATE TABLE IF NOT EXISTS usuario (
    username VARCHAR(50) PRIMARY KEY UNIQUE,
    senha VARCHAR(200) NOT NULL
);

CREATE TABLE IF NOT EXISTS carrinho (
    codigo INT PRIMARY KEY AUTO_INCREMENT,
    usuario VARCHAR(50), 
    finalizado BOOL DEFAULT 0,
    CONSTRAINT fk_carrinho_usuario FOREIGN KEY (usuario) REFERENCES usuario(username)
);

CREATE TABLE IF NOT EXISTS itens_carrinho (
    codigo INT PRIMARY KEY AUTO_INCREMENT,
    cod_carrinho INT,
    cod_burguer INT,
    quantidade INT,
    CONSTRAINT fk_itens_carrinho FOREIGN KEY (cod_carrinho) REFERENCES carrinho(codigo),
    CONSTRAINT fk_itens_carrinho_burguer FOREIGN KEY (cod_burguer) REFERENCES burguer(codigo)
);


INSERT INTO burguer (produto, descricao, preco, foto) 
VALUES ("Classic DEV", "Pão brioche, carne suculenta e queijo derretido", 25.00, "https://images.pexels.com/photos/1639557/pexels-photo-1639557.jpeg?auto=compress&cs=tinysrgb&w=600"),
("Double Stack", "Dois hambúrgueres, bacon crocante e molho especial.", 38.00, "https://images.pexels.com/photos/2983101/pexels-photo-2983101.jpeg?auto=compress&cs=tinysrgb&w=600"),
("Veggie Script", "Hambúrguer de grão de bico com salada fresca.", 30.00, "https://images.pexels.com/photos/3219483/pexels-photo-3219483.jpeg?auto=compress&cs=tinysrgb&w=600"),
("Java Chicken", "Frango empanado crocante com alface e maionese.", 28.00, "https://images.pexels.com/photos/12034622/pexels-photo-12034622.jpeg"),
("Python Onion", "Anéis de cebola, barbecue e queijo cheddar.", 33.00, "https://images.pexels.com/photos/70497/pexels-photo-70497.jpeg?auto=compress&cs=tinysrgb&w=600"),
("React Salad", "Uma opção leve e reativa para o seu almoço.", 27.00, "https://images.pexels.com/photos/1199957/pexels-photo-1199957.jpeg?auto=compress&cs=tinysrgb&w=600");

INSERT INTO usuario (username, senha) VALUES 
('davi', '123'),
('morais', '2'),
('dev', 'root');

INSERT INTO carrinho (usuario, finalizado) VALUES 
('davi', 0),    -- Carrinho do código 1
('morais', 1),     -- Carrinho do código 2 (já finalizado)
('dev', 0); -- Carrinho do código 3

INSERT INTO itens_carrinho (cod_carrinho, cod_burguer, quantidade) VALUES 
(1, 1, 2), 
(1, 5, 1), 
(2, 2, 1), 
(3, 3, 1), 
(3, 4, 1);

select * from itens_carrinho;
drop database db_burguers;
SELECT codigo, usuario FROM carrinho;