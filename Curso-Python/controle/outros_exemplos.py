#!python3

pessoas = ['Maria', 'João', 'Ana', 'Pedro']
adj = ['Legal', 'Chato']

for p in pessoas:
    for a in adj:
        print(f'{p} é {a}')

for i in [1, 2, 3]:
    pass

for i in range(1, 11):
    if i % 2:
        continue 
    print(i)

for i in range(1, 11):
    if i == 5:
        break # sair do loop 
    print(i)
    
print('Fim!')
