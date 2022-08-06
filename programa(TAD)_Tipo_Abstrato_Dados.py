class complexo:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag


    def imprimir(self):
        return "{} + {}i ".format(self.real, self.imag)

    def __add__(self, outro):
        real = self.real + outro.real
        imag = self.imag + outro.imag
        return complexo(real, imag)

    def __sub__(self, outro):
        real = self.real - outro.real
        imag = self.imag - outro.imag
        return complexo(real, imag)

c = complexo(5,5)
a = complexo(10, 10)

print(c.imprimir())
print(a.imprimir())

