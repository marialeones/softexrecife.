var entrada = require('prompt-sync')();
function calcularMedia(nota1, nota2, nota3) {
    let media = (nota1 + nota2 + nota3) / 3;
    return media.toFixed(2);
  }
  
  let nota1 = parseFloat(entrada("Digite a primeira nota: "));
  let nota2 = parseFloat(entrada("Digite a segunda nota: "));
  let nota3 = parseFloat(entrada("Digite a terceira nota: "));
  
  let media = calcularMedia(nota1, nota2, nota3);
  
  console.log("A média é: " + media);
  