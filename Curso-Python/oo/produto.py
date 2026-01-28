
class produto:
    def __init__(self, nome, preco = 35.99, desc = 0): #init é o construtor da classe
        self.nome = nome 
        self.__preco = preco 
        self.desc = desc
        
        @property
        def preco(self):
            return self.__preco
        
        @preco.setter
        def preco(self, novo_preco):
            if novo_preco >= 0:
                self.__preco = novo_preco 
        
    @property #entendido como variavel
    def preco_final(self):
        return (1-self.desc) * self.__preco 
        
p1 = produto('Livro', 39.99, 0.4) #produto __init__ sem passar preço, usa o valor padrão 
p2 = produto('Marca Pagina', 19.90, 0.2)

p1.preco = - 70
p2.preco = - 1.99

print(p1.nome, p1.preco, p1.desc, p1.preco_final) #Livro 39.99 0.4 23.994
print(p2.nome, p2.preco, p2.desc, p2.preco_final) #passou atríbuto para objeto 