CREATE FUNCTION somar_clientes_por_dia(data date) 
RETURNS integer 
AS $$
  SELECT COUNT(*) FROM clientes 
  WHERE DATE(data_cadastro) = DATE(data);
$$ LANGUAGE SQL;

SELECT somar_clientes_por_dia('2023-04-05');
