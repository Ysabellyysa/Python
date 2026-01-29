#Exercicio para aplicar o conteúdo aprendido
#Como exemplo vou usar um sistema de biblioteca,baseado em livros físicos e virtuais.
#Sistema simples de biblioteca para demonstrar classes,herança e tratamendo de entrada.
#O item físico fala em "Retirada na loja", enquanto o digital fala em "Kindle". 
# O código decide qual usar dependendo do tipo de objeto que está no catálogo.

class item_biblioteca: #classe que represnara um item genérico da biblioteca 
    def __init__(self, titulo, autor, preco):
        self.titulo = titulo
        self.autor = autor
        self._preco = preco #é usado _preco para indicar que é um membro privado
        self.disponivel = True #O atríbuto disponível é booleano para controlar estoque

    @property #ele transforma um método (uma função da classe) num atributo de leitura
    def preco_formado(self): 
        return f'{self._preco: .2f}' 

    def descrever(self):
        #retorna uma string com título, autor e preço 
        return f"'{self.titulo}' por '{self.autor}' | {self._preco: .2f}"

    def realizar_entrega(self):
        #faz o return para entrega padrão de livros fisícos
        return f'Retirada na loja - Apresentar recibo na retirada!'

#A classe livro_digital herda essas características, mas adiciona detalhes específicos
class livro_digital(item_biblioteca):
    #Usa a lógica de criação que já escrevi na classe base para configurar o título, o autor e o preço
    def __init__(self, titulo, autor, preco, tamanho_mb):
        super().__init__(titulo, autor, preco) #chama a classe "mãe"
        self.tamanho_mb = tamanho_mb
        
    def descrever(self):
        #retorna uma string com titulo, preço e tamanho do livro digital
        return f'{self.titulo} (E-book) | Preço: {self._preco} Tamanho: {self.tamanho_mb} MB!'

    def realizar_entrega(self):
        #faz o return para entrega padrão de livros digitais
        return f'E-book disponível em Kindle - Tamanho arquivo {self.tamanho_mb} MB!'
    

#--- Execução 

#As listas são coleções ordenadas e mutáveis (você pode adicionar, remover ou alterar itens).
catalogo = [
    livro_digital("Asas Reluzentes", "Allison Sati", 35.00, 18),
    livro_digital("Os dois morrem no final", "Adam Silvera", 32.90, 15),
    livro_digital("Aprendiz do Vilão", "Hannah Nicole", 29.90, 13),
    livro_digital("Academia dos casos arquivados", "Jennifer Lynn", 31.90, 14),
    item_biblioteca("Las Vegas", "Ana K", 69.00),
    item_biblioteca("Black Swan", "L. Santana", 50.00),
    item_biblioteca("Imperfeitos", "Christina Lauren", 20.00),
    item_biblioteca("Boa garota segredo mortal", "Holly Jackson", 59.90)
    
]

#é usado para guardar informações fixas sobre a biblioteca.
info_biblioteca = {
    "unidade": "Central",
    "total_itens": len(catalogo),
}

print("===Biblioteca Digital===")
#começa a contagem em 1 para ficar mais fácil para o usuário
for i, livro in enumerate(catalogo, start=1):
    print(f"[{i}] {livro.descrever()}")
    
#capturando e validando a escolha do usuário
try:
    opcao = int(input("\nDigite o número do catálogo literário: "))
    #Se a numeração começou em 1, convertemos para o índice 0 subtraindo 1
    if 1 <= opcao <= len(catalogo):
        escolhido = catalogo[opcao - 1]
        #verifica a disponibilidade através do atributo booleano disponível
        if not escolhido.disponivel:
            print("Desculpe, fora de estoque!")
        else:
        #marca como índisponivel e processa a entrega
            escolhido.disponivel = False
        print(f'\nSucesso em sua compra!: {escolhido.titulo} | Autor: {escolhido.autor}')
        #Chamamos o método realizar_entrega comportamento depende do tipo do item
        print(f"Forma de acessar seu pedido: {escolhido.realizar_entrega()}.")
        print(f'\nValor da compra:{escolhido.preco_formado}')
    else:
        print('Opção inválida!')
except ValueError:
    #tratamento dimples de erro caso o usuário não digite um inteiro
    print("Digite um número válido! - Tente Novamente")
    

# List Comprehension: gera lista de títulos ainda disponíveis
# - Usamos list comprehension por ser compacto e expressivo
estoque_restante = [l.titulo for l in catalogo if l.disponivel]
print(f'\nDisponíveis no Catálogo: {estoque_restante}')
        