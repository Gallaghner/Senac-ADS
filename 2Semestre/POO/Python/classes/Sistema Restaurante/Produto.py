class Produto:
    def __init__(self,nome,preco,categoria,descricao):
        self.nome = nome
        self.descricao = descricao
        self.preco = preco
        self.categoria = categoria
    
    def alterar_preco(self,novopreco):
        novopreco = input('Digite o novo preço: R$')
        self.preco = novopreco
    


