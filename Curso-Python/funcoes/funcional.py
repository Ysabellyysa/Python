def soma(a, b):
    return a + b

somar = soma 
print(somar(3, 4))

def operacao_aritmetica(fn, op1, op2):
    return fn(op1, op2)

resultado = operacao_aritmetica(soma, 13, 32)
print(resultado)

# resultado = operacao_aritmetica(sub, 13, 48)
# print(resultado)

def soma_parcial(a):
    def concluir_soma(b): #definição de função interna 
        return a + b 
    return concluir_soma #retorna a função interna 

soma_1 = soma_parcial(1) #1 minuto 
r1 = soma_1(2)
r2 = soma_1(3)
r3 = soma_1(4)

resultado_final = soma_parcial(10)(11)
print(resultado_final, r1, r2, r3)

