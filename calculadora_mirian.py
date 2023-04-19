class Calculadora():
      
    def soma(self, num1: float, num2: float):
        print(f'{num1 + num2}')
        return num1 + num2
    
    def subtracao(self, num1: float, num2: float):
        print(num1 - num2)
        return num1 - num2

    def multiplicacao(self, num1: float, num2: float):
        print(num1*num2)
        return num1*num2

    def divisao(self, num1: float, num2: float):
        print(num1/num2)
        return num1/num2

   
    def potencia(self, num1: float, num2: float):
        print(num1**num2)
        return num1**num2
        
    def porcentagem(self):
        pass
    
     
calculadora = Calculadora()
calculadora.potencia(5,2)