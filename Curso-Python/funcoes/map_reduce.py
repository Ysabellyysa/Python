from functools import reduce #importa a função reduce do módulo functools 

def somar_nota(delta):
    def calc(nota):
        return nota + 1.5
    return calc


notas = [6.4, 7.2, 5.8, 8.4]
notas_finais_1 = map(somar_nota(1.5), notas)
notas_finais_2 = map(somar_nota(1.5), notas)

print(list(notas_finais_1))  #para ver os resutados precisei converter para lista
print(list(notas_finais_2))

def somar(a, b):
    return a + b 

total = reduce(somar, notas, 0)
print(total)

# for i, nota in enumerate(notas):
#     notas[i] = nota + 1.5
    
# for i in range(len(notas)):
#     notas[i] = notas[i] + 1.5

# map  mapeia uma função a um iterável (lista, tupla, etc) e retorna um map object (iterável)