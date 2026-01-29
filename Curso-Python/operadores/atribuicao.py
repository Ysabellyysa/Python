# Operadores de Atribuição Composta combinam operação com atribuição

resultado = 2
print(f'Inicial: {resultado}')  # 2

resultado += resultado  # resultado = resultado + resultado -> 2 + 2 = 4
print(f'Após +=: {resultado}')  # 4

resultado += 3          # resultado = resultado + 3 -> 4 + 3 = 7
print(f'Após += 3: {resultado}')  # 7

resultado -= 1          # resultado = resultado - 1 -> 7 - 1 = 6
print(f'Após -= 1: {resultado}')  # 6

resultado *= 4          # resultado = resultado * 4 -> 6 * 4 = 24
print(f'Após *= 4: {resultado}')  # 24

resultado /= 2          # resultado = resultado / 2 -> 24 / 2 = 12.0
print(f'Após /= 2: {resultado}')  # 12.0

resultado %= 6          # resultado = resultado % 6 -> 12 % 6 = 0.0
print(f'Resultado final (%=): {resultado}')  # 0.0