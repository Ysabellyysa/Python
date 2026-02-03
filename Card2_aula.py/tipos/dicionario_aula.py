# Dicionários' mapeamentos de chave valor permitem acesso rápido 
# aos valores pela chave

aluno = {
    'nome': 'Maria',  # chave nome com valor string
    'nota': 9.5,      # chave nota com valor numérico
    'ativo': True     # chave ativo com valor booleano
}

print(type(aluno))  # confirma que aluno é do tipo dict 

# Acessando valores por chave
print(aluno['nome'])   # imprime o valor associado à chave nome
print(aluno['nota'])   # imprime a nota
print(aluno['ativo'])  # indica se o aluno está ativo

# Tamanho do dicionário 
print(len(aluno)) 