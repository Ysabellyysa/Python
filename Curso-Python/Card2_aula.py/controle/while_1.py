#!python3
# WHILE: loop que continua enquanto condição é verdadeira

x = 10

# Nota: este loop é INFINITO (x++ em Python é x+=1, então x sempre aumenta)
# enquanto x (não-zero) sempre é verdadeiro
while x:  # problema: x nunca se torna 0
    print(x)
    x += 1  # aumenta x, loop não termina!
print('Fim!')

# Exemplo mais prático: coletar notas até usuário digitar -1
total = 0
qtde = 0
nota = 0

while nota != -1:
    nota = float(input('Informe a nota ou -1 pra sair: '))
    if nota != -1:  # só contabiliza se for válida (diferente de -1)
        qtde += 1
        total += nota

# Calcula e imprime média
print(f'A média da turma é {total / qtde}')
    