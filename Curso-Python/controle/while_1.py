#!python3

x = 10

while x:
    print(x)
    x += 1
print('Fim!')



total = 0
qtde = 0
nota = 0

while nota != -1:
    nota = float(input('Informe o nota ou -1 pra sair: '))
    if nota != -1:
        qtde += 1
        total += nota 
    
print(f'A media das turma é {total / qtde}')
    