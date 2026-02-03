#!python3
# for loop sobre sequências (ranges, listas, strings, dicts, sets, etc)

# for básico com range 0 até 9 
for i in range(10):
    print(i)

print(' ')

# for com range(inicio, fim): 1 até 10 (11 não incluso)
for i in range(1, 11):
    print(i)

print(' ')

# for com range(inicio, fim, passo): começa em 1, vai até 100, pulando de 7 em 7
for i in range(1, 100, 7):
    print(i)

print(' ')

# for com range negativo começa em 20, vai até 0, pulando -3 a cada iteração
for i in range(20, 0, -3):
    print(i)

print(' ')

# for sobre lista
nums = [2, 4, 6, 8]
for n in nums:
    print(n, end=',')  # end=',' imprime vírgula em vez de quebra de linha

print(' ')

# for sobre string itera sobre cada caractere
texto = "Python "
for letra in texto:
    print(letra, end=' ')

print(' ')

for n in {1, 2, 3, 4, 5}:
    print(n, end=' ')

print(' ')

# for sobre dicionário itera sobre chaves
produtos = {
    'nome': 'Caneca',
    'preco': 14.90,
    'desc': 0.5
}

for atrib in produtos:
    print(atrib, "==>", produtos[atrib])

print(' ')

# for com .items() itera sobre pares
for atrib, valor in produtos.items():
    print(atrib, "==>", valor)

print(' ')

# for com .values()  itera sobre valores
for valor in produtos.values():
    print(valor, end=' ')

print(' ')

# for com .keys() itera sobre chaves 
for atrib in produtos.keys():
    print(atrib, end=' ')
    
