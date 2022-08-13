while True:
    try:
        nome = str(input("Digite seu nome completo: "))
        idade = int(input("Informe sua idade: "))
        print(f"{nome}, tem exatamente {idade} anos. ")
        break
    except(ValueError, TypeError, NameError):
        print("As informações estão incorretas. Por favor tente novamente! ")