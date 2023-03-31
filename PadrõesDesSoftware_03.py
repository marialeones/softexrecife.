from abc import ABC, abstractmethod

class Sanduiche(ABC):
    @abstractmethod
    def getDescricao(self):
        pass

    @abstractmethod
    def getCusto(self):
        pass

class FrangoAssado(Sanduiche):
    def getDescricao(self):
        return "Sanduíche de Frango Assado"

    def getCusto(self):
        return 4.50

class Pepperoni(Sanduiche):
    def __init__(self, sanduiche):
        self.sanduiche = sanduiche

    def getDescricao(self):
        return self.sanduiche.getDescricao() + ", Pepperoni"

    def getCusto(self):
        return self.sanduiche.getCusto() + 0.99

class QueijoMussarelaRalado(Sanduiche):
    def __init__(self, sanduiche):
        self.sanduiche = sanduiche

    def getDescricao(self):
        return self.sanduiche.getDescricao() + ", Queijo Mussarela Ralado"

    def getCusto(self):
        return self.sanduiche.getCusto() + 2.00

sanduiche = FrangoAssado()
sanduiche = Pepperoni(sanduiche)
sanduiche = QueijoMussarelaRalado(sanduiche)

print(sanduiche.getDescricao(), "custa $%.2f." % sanduiche.getCusto())
