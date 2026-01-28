from functools import reduce  

alunos = [
    {'nome': 'Maria', 'nota': 8.1},
    {'nome': 'Pedro', 'nota': 7.2},
    {'nome': 'Ana', 'nota': 8.7},
    {'nome': 'Jose', 'nota': 6.4},
    {'nome': 'Paula', 'nota': 6.7}
]

somar = lambda a, b: a + b

alunos_aprovados = [aluno for aluno in alunos if aluno['nota'] >= 7.0]
notas_alunos_aprovados = [aluno['nota'] for aluno in alunos_aprovados]
total = reduce(somar, notas_alunos_aprovados)
print(total / len(alunos_aprovados))