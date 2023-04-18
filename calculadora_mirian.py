class Calculadora():
    def __init__(self, expressao):
        pass
  
    def soma(self, num1: float, num2: float):
        return print(f'{num1 + num2}')
    
    def subtracao(self, num1: float, num2: float):
        return print(num1 - num2)

    def multiplicacao(self, num1: float, num2: float):
        return print(num1*num2)

    def divisao(self, num1: float, num2: float):
        return print(num1/num2)

   
    def potencia(self, num1: float, num2: float):
        print(num1**num2)
        
    def porcentagem(self):
        pass
    
    def imprimir_resultado():
        pass
    
calculadora = Calculadora()
calculadora.subtracao(2,3)
