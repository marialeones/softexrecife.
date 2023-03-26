var entrada = require('prompt-sync')();
var nota1 = parseFloat(entrada("Digite a primeira nota:"));
var nota2 = parseFloat(entrada("Digite a segunda nota:"));
var nota3 = parseFloat(entrada("Digite a terceira nota:"));

let media = (nota1 + nota2 + nota3) / 3;

media >= 7 ? console.log("Aprovado") : console.log("Reprovado");

var nota1 = parseFloat(entrada("Digite a primeira nota:"));
var nota2 = parseFloat(entrada("Digite a segunda nota:"));

var notaMinima = (21 - (nota1 + nota2)) / 3;

console.log(`Para passar com nota 7 no JS, é necessário tirar no mínimo ${notaMinima.toFixed(2)} na próxima prova.`);
