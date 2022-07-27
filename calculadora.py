"""Faça uma função calculadora de dois números com três parâmetros: os dois primeiros serão os números da operação
 e o terceiro será a entrada que definirá a operação a ser executada. Considera a seguinte definição:
1. Soma
2. Subtração
3. Multiplicação
4. Divisão
Caso seja inserido um número de operação que não exista, o resultado deverá ser 0."""

def calculadora(a,b,d):
    c = int(input("Digite a opção a seguir:  (0). Soma   (1). Subtração  (2). Multiplicação  (3). Divisão  "))
    d = input("Escreva qual opção você escolheu: Soma, Subtração, Multiplicação e Divisão: ")
    soma = a + b
    subtracao = a - b
    divisao = a / b
    multiplicaçao = a * b 
    if c == 0:
        print(f"Á soma entre {a} e {b}, corresponde: {soma}. ")
    if c == 1:
        print(f"Á subtração entre {a} e {b}, corresponde: {subtracao}. ")
    if c == 2:
        print(f"Á multiplicação entre {a} e {b}, corresponde: {multiplicaçao}. ")
    if c == 3:
        print(f"Á divisão entre {a} e {b}, corresponde {divisao}. ")
    if c >= 4:
        print("O resultado é 0. ")

calculadora(25,5,1)
