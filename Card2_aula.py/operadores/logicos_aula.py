# Operadores Lógicos combinam ou modificam expressões booleanas

b1 = True
b2 = False
b3 = True

# Operador AND: ambos precisam ser True
print(b1 and b2 and b3)  # False (porque b2 é False)

# Operador OR: pelo menos um precisa ser True
print(b1 or b2 or b3)    # True (porque b1 e b3 são True)

# Operador != não é lógico, mas de comparação (XOR/OU exclusivo)
print(b1 != b2)          # True (True é diferente de False)

# Operador NOT: negação lógica
print(not b1)            # False (negação de True)
print(not b2)            # True (negação de False)

# Combinando operadores lógicos
print(b1 and not b2 and b3)  # True (True and True and True)

x = 3
y = 4

# AND com condição relacional
print(b1 and not b2 and x < y)  # True (True and True and True)


