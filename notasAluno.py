"""Desenvolva um programa que utiliza o nome de um aluno, duas notas e a quantidade de faltas que ele teve.
 Conclua se o aluno está aprovado ou reprovado de acordo com as especificações:
- Se a média do aluno for menor que sete, o sistema deve informar o nome do aluno e que ele está reprovado;
- Se o aluno possuir mais de três faltas, o sistema deve informar o nome do aluno e que ele está reprovado;
- Se a média do aluno for maior ou igual a sete, o sistema deve informar o nome do aluno e que ele está aprovado. """


aluno = (input("Digite o nome do aluno: "))
nota1 = (float(input("Digite a primeira nota: ")))
nota2 = (float(input("Digite a segunda nota: ")))
falta = (int(input("Digite a quantidade de faltas: ")))
media = (nota1 + nota2) /2
print(media)
if media < 7:
    print(aluno,"Você está reprovado! ")
if falta > 3:
    print(aluno,"Você está reprovado! ")
if media >= 7:
    print(aluno,"Parabéns,Você está aprovado! ")

