class Ave:
    def grasnar(self):
        pass

    def voar(self):
        pass

class Pato(Ave):
    def grasnar(self):
        print("Quack")

    def voar(self):
        print("Voando")

class Galinha(Ave):
    def grasnar(self):
        print("Cócóricó")

    def voar(self):
        print("Não sei voar")

class AdaptadorPato(Ave):
    def __init__(self, pato):
        self.pato = pato

    def grasnar(self):
        self.pato.grasnar()

    def voar(self):
        self.pato.voar()

class AdaptadorPatoDemo:
    def teste(self, ave):
        ave.grasnar()
        ave.voar()

pato = Pato()
galinha = Galinha()
adaptador = AdaptadorPato(pato)

print("O pato diz:")
AdaptadorPatoDemo().teste(pato)

print("A galinha diz:")
AdaptadorPatoDemo().teste(galinha)

print("O pato adaptado como galinha diz:")
AdaptadorPatoDemo().teste(adaptador)
