from Produto import Produto

class Pedido:
    def __init__(self, id_pedido, garcom, produtos, status):
        self.id_pedido = id_pedido
        self.garcom = garcom
        self.produtos = produtos
        self.status = status

    def adicionar_produto(self, produto: Produto):
        self.produtos.append(produto)

    def remover_produto(self, produto):
        if produto in self.produtos:
            self.produtos.remove(produto)
            return True
        return False
    
    def calcular_total(self):
        total = 0.0 
        for produto in self.produtos:
            total += produto.preco
        return total
    
    def __str__(self):
        # Retorna uma string identificando o pedido
        return f"Pedido #{self.id_pedido} - Status: {self.status}"

    def alterar_status(self, novo_status: str):
        self.status = novo_status
    
    def resumo_pedido(self):
        total_atual = self.calcular_total()
        
        print(f"Itens: {self.produtos} | Status: {self.status} | Total: R${total_atual:.2f}")