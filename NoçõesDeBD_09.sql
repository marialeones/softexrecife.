CREATE PROCEDURE relatorio_compras_diarias
AS
BEGIN
    SELECT 
        CONVERT(date, data_compra) as data, 
        COUNT(*) as quantidade_produtos_comprados 
    FROM compras 
    WHERE CONVERT(date, data_compra) = CONVERT(date, GETDATE()) 
    GROUP BY CONVERT(date, data_compra);
END
