"""Desenvolva um código que simule uma eleição com três candidatos.
- candidato_X => 889
- candidato_Y => 847
- candidato_Z => 515
- branco => 0
O código deve perguntar se deseja finalizar a votação depois do voto. Caso o número do voto não corresponda
a nenhum candidato ou seja branco, ele deve ser tratado como nulo. Se for inserido um texto ao invés de número, o código deve 
retornar uma mensagem para votar novamente.
Quando a votação for finalizada, o código deverá mostrar o vencedor, aquele com o maior número de votos e, também, a quantidade 
de votos de cada candidato, os brancos e nulos."""

import enum
class candidato(enum.Enum):
      candidato_X = 889
      candidato_Y = 847
      candidato_Z = 515
      banco = 0

votar = True
votosX = 0
votosY = 0
votosZ = 0
votosBranco = 0 
votosNulo = 0


while votar: 
    votoInvalido = True
    voto = -1
    while votoInvalido:
        try:
            voto = int(input("Informe seu voto: "))
            votoInvalido = False
        except:
            print("Informe um valor válido. ")
    if candidato.candidato_X.value == voto:
        votosX += 1
    elif candidato.candidato_Y.value == voto:
        votosY += 1
    elif candidato.candidato_Z.value == voto:
        votosZ += 1 
    elif candidato.banco.value == voto:
        votosBranco += 1
    else:
        votosNulo +=1 
    
    opcao = int(input("Deseja continuar votando?  => (0) Sim  => (1) Não  "))
    if opcao == 0:
        votar = True
    if opcao == 1: 
        votar = False

print("Votos para o candidato {}: {} ".format(candidato.candidato_X.name, votosX))
print("Votos para candidato {}: {}".format(candidato.candidato_Y.name, votosY))
print("Votos para candidato {}: {}".format(candidato.candidato_Z.name, votosZ))
print("Votos nulos: {}".format(votosNulo))
print("Votos brancos: {}".format(votosBranco))


