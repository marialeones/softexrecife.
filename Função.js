// 1. Função tradicional sem parâmetros
function mensagem() {
    console.log("Olá, mundo!");
  }
  
  mensagem();
  
  // 2. Função tradicional com parâmetros e retorno de valor
  function somar(a, b) {
    return a + b;
  }
  
  const resultado = somar(5, 10);
  console.log(resultado);
  
  // 3. Arrow function com parâmetros e retorno de valor
  const multiplicar = (a, b) => a * b;
  
  const resultado2 = multiplicar(3, 4);
  console.log(resultado2);
  