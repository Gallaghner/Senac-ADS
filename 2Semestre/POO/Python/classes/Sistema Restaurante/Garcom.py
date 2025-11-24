from Pedido import Pedido

class Garcom:
    def __init__(self, id, nome, pedidos_atendidos=None):
        self.id = id
        self.nome = nome
        if pedidos_atendidos is None:
            self.pedidos_atendidos = []
        else:
            self.pedidos_atendidos = pedidos_atendidos        

    def registrar_pedido(self, id_pedido, lista_produtos):
        # 1. Cria o pedido passando 'self' (o próprio garçom)
        novo_pedido = Pedido(id_pedido, self, lista_produtos, "Aberto")
        
        # 2. Salva na lista do garçom
        self.pedidos_atendidos.append(novo_pedido)
        
        print(f"Pedido {id_pedido} registrado pelo garçom {self.nome}")
        
        # 3. Retorna o pedido criado para o sistema usar
        return novo_pedido

    def __str__(self):
        return f"Garçom: {self.nome} (ID: {self.id})"