# herança permite que uma classe (subclasse) herde atributos e métodos de outra (superclasse)

class Carro:
    """Classe base que define comportamento de carros"""
    def __init__(self):
        self.__velocidade = 0  # atributo privado (com __)
        
    @property  # propriedade: permite acessar como carro.velocidade
    def velocidade(self):
        return self.__velocidade
        
    def acelerar(self):
        """Aumenta velocidade em 5 km/h"""
        self.__velocidade += 5
        return self.__velocidade
    
    def frear(self):
        """Diminui velocidade em 5 km/h"""
        self.__velocidade -= 5
        return self.__velocidade

# Subclasse que herda de Carro
class Uni(Carro):
    pass

# Subclasse que herda de Carro o método acelerar
class Ferrari(Carro):
    def acelerar(self):
        """Ferrari acelera 2x mais rápido"""
        super().acelerar()  # chama o método da classe 
        return super().acelerar()  # chama novamente, total +10
    
c1 = Ferrari()
print(c1.acelerar())  # 10 (dois acessos de +5 cada)
print(c1.acelerar())  # 20
print(c1.acelerar())  # 30
print(c1.frear())     # 25 
print(c1.frear())     # 20
print(c1.frear())     # 15 

