#!python3
# funcoes basicas definição, parâmetros, retorno

def saudacao(nome='Pessoa', idade=20):
    """
    Função com parâmetros padrão.
    Se não passar argumentos usa os valores padrão.
    """
    print(f'Bom dia {nome}! \nVocê nem parece ter {idade} anos!')

def soma_e_multi(a, b, x):
    """Retorna resultado de: a + b * x"""
    return a + b * x

# Ponto de entrada 
if __name__ == '__main__':
    saudacao('Ana', idade=30)  # chama com argumentos específicos

# def saudacao():
#     print('Boa Tarde!')

