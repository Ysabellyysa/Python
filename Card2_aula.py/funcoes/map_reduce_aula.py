# map com funções que retornam funções 

from functools import reduce  # importa função reduce

def somar_nota(delta):
    """
    Closure que retorna função para adicionar delta a uma nota.
    Exemplo de função que retorna função
    """
    def calc(nota):
        return nota + 1.5  # nota adiciona 1.5 fixo 
    return calc

notas = [6.4, 7.2, 5.8, 8.4]

# map aplica somar_nota(1.5) a cada nota 
notas_finais_1 = map(somar_nota(1.5), notas)
notas_finais_2 = map(somar_nota(1.5), notas)

# Converte para lista para visualizar 
print(list(notas_finais_1))  # [7.9, 8.7, 7.3, 9.9]
print(list(notas_finais_2))  # [7.9, 8.7, 7.3, 9.9]

# reduce soma todas as notas
def somar(a, b):
    return a + b

total = reduce(somar, notas, 0)  # começa de 0, soma todas as notas
print(total)  # 27.8

# for i, nota in enumerate(notas):
#     notas[i] = nota + 1.5
#
# for i in range(len(notas)):
#     notas[i] = notas[i] + 1.5
