from functools import reduce #importa a função reduce do módulo functools 

alunos = [
    {'nome': 'Maria', 'nota': 8.1},
    {'nome': 'Pedro', 'nota': 7.2},
    {'nome': 'Ana', 'nota': 8.7},
    {'nome': 'Jose', 'nota': 6.4},
    {'nome': 'Paula', 'nota': 6.7}
]

aluno_aprovado = lambda aluno: aluno['nota'] >= 7.0
# aluno_honra = lambda aluno: aluno['nota'] >= 9.0
obter_nota = lambda aluno: aluno['nota']
somar = lambda a, b: a + b

alunos_aprovados = filter(aluno_aprovado, alunos) 
notas_alunos_aprovados = list(map(obter_nota, alunos_aprovados))
total = reduce(somar, notas_alunos_aprovados)

# The code snippet you provided is demonstrating the use of lambda functions, filter, map, and print
# statements in Python.
# print(obter_nota(alunos[2]))

# print(alunos)
print(total)
print(total / len(notas_alunos_aprovados))
# print(notas_alunos_aprovados) #filter retorna objeto iterável, converti para lista 