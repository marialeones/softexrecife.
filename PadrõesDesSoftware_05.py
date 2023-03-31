from abc import ABC, abstractmethod

class Strategy(ABC):
    @abstractmethod
    def execute(self, num1: int, num2: int) -> int:
        pass

class Soma(Strategy):
    def execute(self, num1: int, num2: int) -> int:
        return num1 + num2

class Subtracao(Strategy):
    def execute(self, num1: int, num2: int) -> int:
        return num1 - num2

class Multiplicacao(Strategy):
    def execute(self, num1: int, num2: int) -> int:
        return num1 * num2

class Calculadora:
    def __init__(self):
        self.operacoes = {'+': Soma(), '-': Subtracao(), '*': Multiplicacao()}

    def calcular(self):
        num1 = int(input("Digite o primeiro número: "))
        num2 = int(input("Digite o segundo número: "))
        op = input("Digite a operação (+, -, *): ")
        if op not in self.operacoes:
            print("Operação inválida")
            return
        resultado = self.operacoes[op].execute(num1, num2)
        print(f"Resultado: {resultado}")

calculadora = Calculadora()
calculadora.calcular()
