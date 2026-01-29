#!python3
# estrutura condicional com múltiplas ramificações

nota = float(input("Informe a nota do aluno: "))
comportado = True if input('Comportado? (s/n) ') == 'y' else False

# Condicionais em cascata
if nota >= 9 and comportado:
    print('Duas palavras: Para Bens! :p')
    print('Quadro de Honra!')
elif nota >= 7:
    print('Água bateu na bunda, mais aprovado! :)')
elif nota >= 5.5:
    print('Recuperação, se recupere!')
elif nota >= 4.3:
    print('Vai estudar mais, quase reprovado!')
else:
    print('Duas palavras: Reprovado!')

print(nota)