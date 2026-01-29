# PROPRIEDADES (@property) e SETTERS controle de acesso a atributos

class Produto:
    def __init__(self, nome, preco=35.99, desc=0):
        """Construtor da classe Produto."""
        self.nome = nome
        self.__preco = preco  # atributo privado 
        self.desc = desc
        
    @property  #transforma método em propriedade
    def preco(self):
        """Getter: permite ler preco como p1.preco (sem parênteses)"""
        return self.__preco
    
    @preco.setter  # define como modificar o atributo preco
    def preco(self, novo_preco):
        """Setter: valida novo preço antes de atribuir"""
        if novo_preco >= 0:  # só aceita preços positivos
            self.__preco = novo_preco
    
    @property
    def preco_final(self):
        """Propriedade calculada: preco com desconto aplicado"""
        return (1 - self.desc) * self.__preco

# Criando instâncias
p1 = Produto('Livro', 39.99, 0.4)  # 40% de desconto
p2 = Produto('Marca Pagina', 19.90, 0.2)  # 20% de desconto

# Tentando atribuir preços negativos 
p1.preco = -70  # setter rejeita valores negativos, mantém 39.99
p2.preco = -1.99  # setter rejeita valores negativos, mantém 19.90

# Exibindo informações
print(p1.nome, p1.preco, p1.desc, p1.preco_final)  # Livro 39.99 0.4 23.994
print(p2.nome, p2.preco, p2.desc, p2.preco_final)  # Marca Pagina 19.90 0.2 15.92 