from copy import deepcopy


class Veiculo:
  def __init__(self, modelo, marca, cor, numeroRodas):
    self.modelo = modelo
    self.marca = marca
    self.cor = cor
    self.numeroRodas = numeroRodas

  def clone(self):
    return deepcopy(self)

  def represent(self):
    return f"Modelo: {self.modelo}, Marca: {self.marca}, Cor: {self.cor}, Número de rodas: {self.numeroRodas}"



class Carro(Veiculo):
  def __init__(self, modelo, marca, cor, numeroRodas, numeroPortas):
    super().__init__(modelo, marca, cor, numeroRodas)
    self.numeroPortas = numeroPortas

  def represent(self):
    return f"Modelo: {self.modelo}, Marca: {self.marca}, Cor: {self.cor}, Número de rodas: {self.numeroRodas}, Número de portas: {self.numeroPortas}"



class Moto(Veiculo):
  def __init__(self, modelo, marca, cor, numeroRodas, tipo):
    super().__init__(modelo, marca, cor, numeroRodas)
    self.tipo = tipo

  def represent(self):
    return f"Modelo: {self.modelo}, Marca: {self.marca}, Cor: {self.cor}, Número de rodas: {self.numeroRodas}, Tipo: {self.tipo}"



class Aplicacao:
  def __init__(self):
    self.veiculos = [
      Carro("Fiesta", "Ford", "Preto", 4, 4),
      Carro("Cruze", "Chevrolet", "Branco", 4, 4),
      Moto("CG 160", "Honda", "Azul", 2, "Street"),
      Moto("MT-07", "Yamaha", "Vermelho", 2, "Naked"),
      Carro("Corolla", "Toyota", "Prata", 4, 4),
      Moto("CBR 1000RR", "Honda", "Vermelho", 2, "Esportiva")
    ]

  def clone_veiculos(self):
    return [veiculo.clone() for veiculo in self.veiculos]

  def represent_clone_veiculos(self):
    clones = self.clone_veiculos()
    for clone in clones:
      print(clone.represent())



app = Aplicacao()
app.represent_clone_veiculos()
