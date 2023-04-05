CREATE TABLE produtos (
  id INT PRIMARY KEY,
  nome VARCHAR(50),
  preco DECIMAL(10,2),
  estoque INT
);

CREATE TABLE vendas (
  id INT PRIMARY KEY,
  data DATE,
  produto_id INT,
  quantidade INT,
  FOREIGN KEY (produto_id) REFERENCES produtos(id)
);

CREATE TRIGGER tr_vendas AFTER INSERT ON vendas
FOR EACH ROW
BEGIN
  UPDATE produtos SET estoque = estoque - NEW.quantidade WHERE id = NEW.produto_id;
END;
