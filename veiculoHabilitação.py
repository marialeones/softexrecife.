"""Desenvolva um código que utilize as seguintes características de um veículo:
- Quantidade de rodas;
- Peso bruto em quilogramas;
- Quantidade de pessoas no veículo.
Com essas informações, o programa mostrará qual é a melhor categoria de habilitação para o veículo informado a partir das condições:
A: Veículos com duas ou três rodas;
B: Veículos com quatro rodas, que acomodam até oito pessoas e seu peso é de até 3500 kg;
C: Veículos com quatro rodas ou mais e com peso entre 3500 e 6000 kg;
D: Veículos com quatro rodas ou mais e que acomodam mais de oito pessoas;
E: Veículos com quatro rodas ou mais e com mais de 6000 kg."""

rodas = int(input("Digite á quantidade de rodas do seu veículo: "))
kg = int(input("Digite o Peso bruto em quilogramas do veículo: peso; (até 3500 Kg), (3500 e 6000 Kg), ( mais de 6000 kg)  "))
pessoas = int(input("Digite Quantidade de pessoas no veículo: "))
if rodas == 2 or 3: 
    print("habilitaçâo CNH da categoria A. ")
if rodas == 4 and pessoas <= 8 and kg <= 3500:
    print("habilitação CNH da categoria B. ")
if rodas >= 4 and kg > 3500 and 6000:
    print("habilitação CNH da categoria C.")
if rodas >= 4 and pessoas > 8:
    print("habilitação CNH da categoria D.")
if rodas >= 4 and kg > 6000:
    print("habilitação CNH da categoria E") 


