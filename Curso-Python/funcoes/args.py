# *args E **kwargs argumentos variáveis

def soma(*nums):
    """
    Soma um número variável de argumentos.
    *nums captura argumentos posicionais como tupla
    """
    total = 0
    for n in nums:
        total += n
    return total

def resultado_final(**kwargs):
    """
    Função que aceita argumentos nomeados variáveis.
    **kwargs captura argumentos nomeados como dicionário
    """
    status = 'Aprovado(a)' if kwargs['nota'] >= 7 else 'Reprovado(a)'
    return f'{kwargs["nome"]} foi {status}' 
