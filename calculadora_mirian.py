class Calculadora():
    def __init__(self, numero1: float, numero2: float):
        self.numero1 = numero1
        self.numero2 = numero2 
        print(f'Os numeros escolhidos são {self.numero1} e {self.numero2}')
  
    def soma(self):
        return self.numero1 + self.numero2
  
Calculadora(1,2)