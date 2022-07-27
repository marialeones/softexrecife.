"""Faça uma função calculadora que os números e as operações serão feitas pelo usuário. O código deve ficar rodando infinitamente
 até que o usuário escolha a opção de sair. No início, o programa mostrará a seguinte lista de operações:
1: Soma
2: Subtração
3: Multiplicação
4: Divisão
0: Sair
Digite o número para a operação correspondente e caso o usuário introduza qualquer outro, o sistema deve mostrar a mensagem 
“Essa opção não existe” e voltar ao menu de opções.
Após a seleção, o sistema deve pedir para o usuário inserir o primeiro e segundo valor, um de cada. Depois precisa executar 
a operação e mostrar o resultado na tela. Quando o usuário escolher a opção “Sair”, o sistema irá parar. 
É necessário que o sistema mostre as opções sempre que finalizar uma operação e mostrar o resultado."""

def calculadora(*num):
    while True:
        print('escolha uma opção: ')
        print(' (1): Soma.')
        print(' (2): Subtração.')
        print(' (3): Multiplicação.')
        print(' (4): Divisão.')
        print(' (0): Sair. ')

        opcao = int(input("Digite uma opção: "))
        n1 = int(input("Informe o primeiro número: "))
        n2 = int(input("Informe o segundo número: "))

        if opcao == 1:
            soma = n1 + n2
            print(f"Á soma entre {n1} e {n2}, corresponde á: {soma}. ")
        if opcao == 2:
            subtracao = n1 - n2
            print(f"Á subtração entre {n1} e {n2}, corresponde á: {subtracao}. ")
        if opcao == 3:
            multiplicacao = n1 * n2
            print(f"À multiplicação entre {n1} e {n2}, corresponde á: {multiplicacao}. ")
        if opcao == 4:
            divisao = n1 / n2
            print(f"Á divisão entre {n1} e {n2}, corresponde á: {divisao}. ")
        if opcao >= 5:
            print("Essa opção não existe")
        if opcao == 0:
            print("Até logo! ")
            break
        
calculadora()

      
    

   