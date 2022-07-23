"""Faça um código que execute a contagem regressiva de uma bomba, informando o número de segundos para explodir.
 Ele deverá mostrar a mensagem “iniciando contagem regressiva”, os segundos passados e, no final, a mensagem “BUM!”. """


import time

bomba = 0
tempoExplodir = 15

print("Iniciando contagem regressiva...")
for i in range(bomba,tempoExplodir+1):
    print(i)

    time.sleep(1)
print("BUUM!")
