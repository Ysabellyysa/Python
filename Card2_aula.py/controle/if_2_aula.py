#!python3

# Exemplos de valores que são considerados falsos 
a = 'valor'  # string não-vazia é verdadeira
a = 0  # zero é falso
a = -1  # números negativos são verdadeiros 
a = ''  # string vazia é falsa
a = '  '  # string com espaços verdadeira
a = []  # lista vazia é falsa
a = {}  # dicionário vazio é falso

if a:  # avalia a como True ou False
    print('Existe')
else:
    print('Não existe')  # imprime Não existe pois {} é falso