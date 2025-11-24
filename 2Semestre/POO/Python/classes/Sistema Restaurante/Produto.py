class Produto:
    def __init__(self, nome, preco, categoria, descricao):
        self.nome = nome
        self.preco = preco
        self.categoria = categoria
        self.descricao = descricao

    def alterar_preco(self, novo_preco):
        self.preco = novo_preco

    def __repr__(self):
        return self.nome