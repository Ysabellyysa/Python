#!python3

a = 'valor'
a = 0
a = -1
a = ''  #espaços em branco também são considerados vazios e falsos 
a = '  '
a = []  #listas vazias são consideradas falsas 
a = {} #dicionários vazios são considerados falsos 
if a:
    print('Existe')
else:
    print('Não existe')