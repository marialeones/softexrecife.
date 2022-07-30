"""Desenvolva um programa que recebe do usuário nome completo e ano de nascimento que seja entre 1922 e 2021.
 A partir dessas informações, o sistema mostrará o nome do usuário e a idade que completou, ou completará, no ano atual (2022).
Caso o usuário não digite um número ou apareça um inválido no campo do ano, o sistema informará o erro e 
continuará perguntando até que um valor correto seja preenchido."""

from datetime import date

def codigo():
 while True:
    try: 
     nome = input("Digite seu nome completo: ")
     ano = int(input("Digite o ano de nascimento: (entre 1922 e 2021) "))
     anoAtual = date.today().year 
     idade = anoAtual - ano 
     print(f"O seu nome é: {nome}, sua idade é: {idade} anos.   ")
    except(ValueError, TypeError):
        print("\033[31mERRO! Tente novamente! \033[m")
        continue
    else:
        print("Àte logo! ")
        break


codigo()
  
