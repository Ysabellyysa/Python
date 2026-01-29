# FILTER, MAP, REDUCE operações funcionais sobre coleções

from functools import reduce  # importa função reduce do módulo functools

alunos = [
    {'nome': 'Maria', 'nota': 8.1},
    {'nome': 'Pedro', 'nota': 7.2},
    {'nome': 'Ana', 'nota': 8.7},
    {'nome': 'Jose', 'nota': 6.4},
    {'nome': 'Paula', 'nota': 6.7}
]

# lambda funções anônimas de uma linha
aluno_aprovado = lambda aluno: aluno['nota'] >= 7.0  # retorna True se aprovado
obter_nota = lambda aluno: aluno['nota']  # extrai apenas a nota
somar = lambda a, b: a + b  # soma dois números

# filter filtra elementos que atendem critério retorna iterável
alunos_aprovados = filter(aluno_aprovado, alunos)

# map aplica função a cada elemento retorna iterável
notas_alunos_aprovados = list(map(obter_nota, alunos_aprovados))

# reduce acumula resultado aplicando função a pares de elementos
total = reduce(somar, notas_alunos_aprovados)

# Imprime total e média
print(total)
print(total / len(notas_alunos_aprovados))

# aluno_honra = lambda aluno: aluno['nota'] >= 9.0
# print(obter_nota(alunos[2]))  # debug pega nota do aluno índice 2
# print(alunos)  # debug imprime lista completa
# print(notas_alunos_aprovados)  # nota filter retorna iterável, convertemos para lista 