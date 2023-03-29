// criando o objeto
const pessoa = {
    nome: "Maria",
    idade: 28,
    cidade: "Pernambuco"
  };
  
  // criação do array
  const frutas = ["pera", "abacate", "morango"];
  
  // função para listar as propriedades do objeto
  function listarPropriedades(objeto) {
    for (let propriedade in objeto) {
      console.log(propriedade);
    }
  }
  
  // função para listar os elementos do array
  function listarElementos(array) {
    for (let i = 0; i < array.length; i++) {
      console.log(array[i]);
    }
  }
  
  // chamada das funções para listar as propriedades do objeto e os elementos do array
  listarPropriedades(pessoa);
  listarElementos(frutas);
  