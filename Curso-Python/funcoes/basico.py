#!python3

def saudacao(nome = 'Pessoa', idade = 20): #toda função em python define em bloco 
    print(f'Bom dia {nome}! \n Voce nem parece ter {idade} anos!')
    

def soma_e_multi(a, b, x):
    return a + b * x


if __name__ == '__main__':
    saudacao('Ana', idade = 30)

# def saudacao():
#     print('Boa Tarde!')

