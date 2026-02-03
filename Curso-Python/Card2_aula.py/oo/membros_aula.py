#!python3
# membros são atributos e métodos estáticos

class Contador:
    contador = 0  # Atributo de classe

    def inc_maluco(self):
        """Método de instância que cria um atributo local de instância"""
        self.contador = self.contador + 1  # cria atributo em self, não modifica a classe
        return self.contador
    
    @classmethod  # método de classe recebe a classe como parâmetro cls
    def inc(cls):
        """Incrementa o atributo de classe"""
        cls.contador += 1  # modifica o atributo compartilhado
        return cls.contador
    
    @classmethod  # método de classe
    def dec(cls):
        """Decrementa o atributo de classe"""
        cls.contador -= 1
        return cls.contador
    
    @staticmethod  # método estático não precisa de self ou cls
    def mais_um(n):
        """Função utilitária que não acessa estado da classe"""
        return n + 1
    
# Testando método de instância (incrivelmente)
c1 = Contador()
print(c1.inc_maluco())  # 1 (cria atributo local em c1)
print(c1.inc_maluco())  # 2 (usa atributo local de c1)
print(c1.inc_maluco())  # 3
print(c1.inc_maluco())  # 4

# Testando método de classe (modifica o contador compartilhado)
print(Contador.inc())   # 1 (incrementa o contador de classe)
print(Contador.inc())   # 2

# print(Contador.inc())   # 3
# print(Contador.dec())   # 2 
# print(Contador.dec())   # 1
# print(Contador.dec())   # 0
# print(Contador.mais_um(99))  