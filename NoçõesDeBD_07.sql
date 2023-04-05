CREATE TABLE Cliente (
    Id INT PRIMARY KEY,
    Nome VARCHAR(50),
    Endereco VARCHAR(100)
);

CREATE TABLE Pedido (
    Id INT PRIMARY KEY,
    DataPedido DATE,
    ValorTotal DECIMAL(10,2),
    ClienteId INT,
    FOREIGN KEY (ClienteId) REFERENCES Cliente(Id)
);

CREATE TABLE ItemPedido (
    Id INT PRIMARY KEY,
    Produto VARCHAR(50),
    Quantidade INT,
    ValorUnitario DECIMAL(10,2),
    PedidoId INT,
    FOREIGN KEY (PedidoId) REFERENCES Pedido(Id)
);


INSERT INTO Cliente (Id, Nome, Endereco)
VALUES (1, 'João', 'Rua A, 123'),
       (2, 'Maria', 'Rua B, 456'),
       (3, 'Pedro', 'Rua C, 789');

INSERT INTO Pedido (Id, DataPedido, ValorTotal, ClienteId)
VALUES (1, '2022-01-01', 100.00, 1),
       (2, '2022-01-02', 200.00, 2),
       (3, '2022-01-03', 300.00, 3);

INSERT INTO ItemPedido (Id, Produto, Quantidade, ValorUnitario, PedidoId)
VALUES (1, 'Produto 1', 2, 50.00, 1),
       (2, 'Produto 2', 3, 40.00, 1),
       (3, 'Produto 3', 1, 100.00, 2),
       (4, 'Produto 4', 4, 25.00, 3),
       (5, 'Produto 5', 2, 75.00, 3);


SELECT Cliente.Nome, Pedido.DataPedido, Pedido.ValorTotal, ItemPedido.Produto, ItemPedido.Quantidade, ItemPedido.ValorUnitario
FROM Cliente
INNER JOIN Pedido ON Cliente.Id = Pedido.ClienteId
INNER JOIN ItemPedido ON Pedido.Id = ItemPedido.PedidoId;

SELECT Cliente.Nome, Pedido.DataPedido, Pedido.ValorTotal, ItemPedido.Produto, ItemPedido.Quantidade, ItemPedido.ValorUnitario
FROM Cliente
LEFT JOIN Pedido ON Cliente.Id = Pedido.ClienteId
LEFT JOIN ItemPedido ON Pedido.Id = ItemPedido.PedidoId;

SELECT Cliente.Nome, Pedido.DataPedido, Pedido.ValorTotal, ItemPedido.Produto, ItemPedido.Quantidade, ItemPedido.Valor
