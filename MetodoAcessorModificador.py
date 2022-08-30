class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def desconto(self, percentual):
        self.preco = self.preco - (self.preco * (percentual / 100))

    @property
    def nome(self):
        return self.nome1

    @nome.setter
    def nome(self, valor):
        self.nome1 = valor.title()

    @property
    def preco(self):
        return self.preco1

    @preco.setter
    def preco(self, valor):
        if isinstance(valor, str):
            valor = float(valor.replace('R$', ''))

        self.preco1 = valor

p1 = Produto('SAPATO', 100)
p1.desconto(10)
print(p1.nome, p1.preco)

p2 = Produto('TABlet', 'R$800')
p2.desconto(25)
print(p2.nome, p2.preco)

