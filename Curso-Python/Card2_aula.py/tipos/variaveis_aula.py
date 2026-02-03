a = 3 #inteiro
b = 4.4 #float 

print(a + b) #imprime a soma de a e b

texto = "Sua Idade é..." #string > imprime o texto
idade = 23 #inteiro > imprime a idade 

print(texto, str(idade)) #texto com idade convertida para string 
print(f'{texto} {idade}') #f-string forma moderna de interpolação

saudacao = "Bom dia! " #string > imprime a saudação 
print(3 * saudacao) #imprime a saudação 3 vezes 

PI = 3.14 #constante > valor de PI 
raio = float(input('Informe o raio da circunferência: ')) #float > lê o valor do raio informado

area = PI * pow(raio, 2) #calcula a área da circunferência 

print(f'A área da circ é {area} m2.') #imprime a área da circunferência