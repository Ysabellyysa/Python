#!python3 

for i in range(10):
  print(i)
    
print(' ')

for i in range(1, 11):
  print(i)

print(' ')

for i in range(1, 100, 7):
  print(i)

print(' ')
    
for i in range(20, 0, -3):
   print(i)

print(' ')

nums = [2, 4, 6, 8]

for n in nums:
  print(n, end=',')

print(' ')

texto = "Python "

for letra in texto:
   print(letra, end=' ') 
   
print(' ')
    
for n in {1, 2, 3, 4, 5}:
   print(n, end=' ')

print(' ')

produtos= {
    'nome': 'Caneca',
    'preco': 14.90,
    'desc': 0.5 
}

for atrib in produtos:
   print(atrib, "==>", produtos[atrib])

print(' ')    

for atrib, valor in produtos.items():
    print(atrib, "==>", valor)

print(' ')
    
for valor in produtos.values():
    print(valor, end=' ')

print(' ')    
    
for atrib in produtos.keys():
    print(atrib, end=' ')
    
