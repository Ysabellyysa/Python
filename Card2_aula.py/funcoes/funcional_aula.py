# funções como valores, higher-order functions, closures

def soma(a, b):
    """Função simples que soma dois números"""
    return a + b

# Atribui função a uma variável
somar = soma
print(somar(3, 4))  # 7

# Higher-order function recebe função como parâmetro
def operacao_aritmetica(fn, op1, op2):
    """Executa a função fn com os operandos op1 e op2"""
    return fn(op1, op2)

resultado = operacao_aritmetica(soma, 13, 32)
print(resultado)  # 45

# def subtracao(a, b):
#     return a - b
# resultado = operacao_aritmetica(subtracao, 13, 48)
# print(resultado)

# função interna que captura variáveis da função externa
def soma_parcial(a):
    """
    Retorna uma função que soma a a qualquer número.
    Exemplo de closure concluir_soma lembra do valor de a
    """
    def concluir_soma(b):
        return a + b
    return concluir_soma

soma_1 = soma_parcial(1)  # cria função que soma 1 a tudo
r1 = soma_1(2)  # 1 + 2 = 3
r2 = soma_1(3)  # 1 + 3 = 4
r3 = soma_1(4)  # 1 + 4 = 5

# Chamar diretamente sem atribuir a variável
resultado_final = soma_parcial(10)(11)  # 10 + 11 = 21
print(resultado_final, r1, r2, r3)  # 21 3 4 5

