#list comprehension e reduce forma concisa de trabalhar com listas


from functools import reduce  # importa função reduce

alunos = [
    {'nome': 'Maria', 'nota': 8.1},
    {'nome': 'Pedro', 'nota': 7.2},
    {'nome': 'Ana', 'nota': 8.7},
    {'nome': 'Jose', 'nota': 6.4},
    {'nome': 'Paula', 'nota': 6.7}
]

# Lambda para somar dois valores
somar = lambda a, b: a + b

# List comprehension filtra alunos com nota >= 7
alunos_aprovados = [aluno for aluno in alunos if aluno['nota'] >= 7.0]

# List comprehension extrai apenas as notas dos aprovados
notas_alunos_aprovados = [aluno['nota'] for aluno in alunos_aprovados]

# Reduce soma todas as notas percorre lista acumulando resultado
total = reduce(somar, notas_alunos_aprovados)

# Calcula média dos aprovados
print(total / len(alunos_aprovados))