from datetime import datetime, date

class Cliente:
    def __init__(self, identificacao, nome, cpf, email, telefone):
        self.identificacao = identificacao
        self.nome = nome
        self.cpf = cpf
        self.email = email
        self.telefone = telefone
        self.pedidos = []
    
    def cadastrar(self):
        """Cadastra o cliente no sistema"""
        print(f"Cliente {self.nome} cadastrado com sucesso!")
        print(f"ID: {self.identificacao}")
        return True
    
    def atualizar_cadastro(self, **kwargs):
        """Atualiza o cadastro do cliente"""
        for chave, valor in kwargs.items():
            if hasattr(self, chave):
                setattr(self, chave, valor)
        print(f"Cadastro de {self.nome} atualizado!")
    
    def consultar_pedidos(self):
        """Consulta todos os pedidos realizados pelo cliente"""
        if not self.pedidos:
            print(f"{self.nome} não possui pedidos realizados.")
            return []
        
        print(f"\nPedidos de {self.nome}:")
        for pedido in self.pedidos:
            print(f"- Pedido: {pedido.identificador}")
            print(f"  Data: {pedido.data}")
            print(f"  Valor Total: R$ {pedido.valor_total:.2f}")
            print(f"  Status: {pedido.status}")
            print()
        return self.pedidos


class Produto:
    def __init__(self, codigo, nome, descricao, preco, quantidade_estoque):
        self.codigo = codigo
        self.nome = nome
        self.descricao = descricao
        self.preco = preco
        self.quantidade_estoque = quantidade_estoque
    
    def atualizar_estoque(self, quantidade):
        """Atualiza a quantidade em estoque"""
        self.quantidade_estoque += quantidade
        print(f"Estoque de {self.nome} atualizado: {self.quantidade_estoque} unidades")
        return self.quantidade_estoque
    
    def aplicar_desconto(self, percentual):
        """Aplica um desconto ao produto"""
        desconto = self.preco * (percentual / 100)
        preco_com_desconto = self.preco - desconto
        print(f"Desconto de {percentual}% aplicado em {self.nome}")
        print(f"Preço original: R$ {self.preco:.2f}")
        print(f"Preço com desconto: R$ {preco_com_desconto:.2f}")
        return preco_com_desconto
    
    def exibir_informacoes(self):
        """Exibe informações detalhadas do produto"""
        info = f"""
        ===== PRODUTO =====
        Código: {self.codigo}
        Nome: {self.nome}
        Descrição: {self.descricao}
        Preço: R$ {self.preco:.2f}
        Estoque: {self.quantidade_estoque} unidades
        ===================
        """
        print(info)
        return info


class ItemPedido:
    def __init__(self, codigo, produto, quantidade, preco_unitario):
        self.codigo = codigo
        self.produto = produto
        self.quantidade = quantidade
        self.preco_unitario = preco_unitario
        self.subtotal = self.calcular_subtotal()
    
    def calcular_subtotal(self):
        """Calcula o subtotal do item"""
        self.subtotal = self.quantidade * self.preco_unitario
        return self.subtotal
    
    def atualizar_quantidade(self, nova_quantidade):
        """Atualiza a quantidade do item"""
        self.quantidade = nova_quantidade
        self.calcular_subtotal()
        print(f"Quantidade de {self.produto.nome} atualizada para {nova_quantidade}")
        print(f"Novo subtotal: R$ {self.subtotal:.2f}")
    
    def exibir_informacoes(self):
        """Exibe informações do item"""
        info = f"""
        Item: {self.produto.nome}
        Código: {self.codigo}
        Quantidade: {self.quantidade}
        Preço Unitário: R$ {self.preco_unitario:.2f}
        Subtotal: R$ {self.subtotal:.2f}
        """
        print(info)
        return info


class Pedido:
    def __init__(self, identificador, data, cliente):
        self.identificador = identificador
        self.data = data
        self.cliente = cliente
        self.valor_total = 0.0
        self.status = "Aberto"
        self.itens = []
        self.pagamento = None
        cliente.pedidos.append(self)
    
    def adicionar_produto(self, produto, quantidade):
        """Adiciona um produto ao pedido"""
        # Verifica se há estoque suficiente
        if produto.quantidade_estoque < quantidade:
            print(f"Estoque insuficiente de {produto.nome}")
            print(f"Disponível: {produto.quantidade_estoque} unidades")
            return False
        
        # Cria um item de pedido
        codigo_item = f"ITEM{len(self.itens) + 1:03d}"
        item = ItemPedido(codigo_item, produto, quantidade, produto.preco)
        self.itens.append(item)
        
        # Atualiza o estoque do produto
        produto.atualizar_estoque(-quantidade)
        
        print(f"{quantidade}x {produto.nome} adicionado ao pedido")
        self.calcular_valor_total()
        return True
    
    def remover_produto(self, codigo_item):
        """Remove um produto do pedido"""
        for item in self.itens:
            if item.codigo == codigo_item:
                # Devolve o estoque
                item.produto.atualizar_estoque(item.quantidade)
                self.itens.remove(item)
                print(f"Item {codigo_item} removido do pedido")
                self.calcular_valor_total()
                return True
        print(f"Item {codigo_item} não encontrado no pedido")
        return False
    
    def calcular_valor_total(self):
        """Calcula o valor total do pedido"""
        self.valor_total = sum(item.subtotal for item in self.itens)
        print(f"Valor total do pedido: R$ {self.valor_total:.2f}")
        return self.valor_total
    
    def exibir_pedido(self):
        """Exibe detalhes completos do pedido"""
        print(f"\n{'='*50}")
        print(f"PEDIDO: {self.identificador}")
        print(f"Cliente: {self.cliente.nome}")
        print(f"Data: {self.data}")
        print(f"Status: {self.status}")
        print(f"{'-'*50}")
        print("ITENS:")
        for item in self.itens:
            print(f"  {item.quantidade}x {item.produto.nome} - R$ {item.preco_unitario:.2f} = R$ {item.subtotal:.2f}")
        print(f"{'-'*50}")
        print(f"VALOR TOTAL: R$ {self.valor_total:.2f}")
        print(f"{'='*50}\n")


class Pagamento:
    def __init__(self, codigo, pedido, forma_pagamento, valor_pago, data):
        self.codigo = codigo
        self.pedido = pedido
        self.forma_pagamento = forma_pagamento
        self.valor_pago = valor_pago
        self.data = data
        self.status = "Pendente"
        pedido.pagamento = self
    
    def processar_pagamento(self):
        """Processa o pagamento do pedido"""
        self.status = "Processando"
        print(f"Processando pagamento {self.codigo}...")
        
        # Verifica se o valor pago é suficiente
        if self.valor_pago < self.pedido.valor_total:
            print(f"Valor insuficiente! Faltam R$ {self.pedido.valor_total - self.valor_pago:.2f}")
            self.status = "Negado"
            return False
        
        # Processa o pagamento
        self.status = "Aprovado"
        self.pedido.status = "Pago"
        print(f"Pagamento aprovado!")
        print(f"Valor: R$ {self.valor_pago:.2f}")
        
        # Calcula troco se houver
        if self.valor_pago > self.pedido.valor_total:
            troco = self.valor_pago - self.pedido.valor_total
            print(f"Troco: R$ {troco:.2f}")
        
        return True
    
    def confirmar(self):
        """Confirma o pagamento"""
        if self.status == "Aprovado":
            self.status = "Confirmado"
            self.pedido.status = "Finalizado"
            print(f"Pagamento {self.codigo} confirmado!")
            return True
        print("Pagamento não pode ser confirmado. Status atual:", self.status)
        return False
    
    def emitir_recibo(self):
        """Emite o recibo do pagamento"""
        if self.status in ["Aprovado", "Confirmado"]:
            troco = self.valor_pago - self.pedido.valor_total if self.valor_pago > self.pedido.valor_total else 0
            
            recibo = f"""
            {'='*50}
                          RECIBO DE PAGAMENTO
            {'='*50}
            Código do Pagamento: {self.codigo}
            Pedido: {self.pedido.identificador}
            Cliente: {self.pedido.cliente.nome}
            CPF: {self.pedido.cliente.cpf}
            {'~'*50}
            Data: {self.data}
            Forma de Pagamento: {self.forma_pagamento}
            {'~'*50}
            Valor do Pedido: R$ {self.pedido.valor_total:.2f}
            Valor Pago: R$ {self.valor_pago:.2f}
            Troco: R$ {troco:.2f}
            {'~'*50}
            Status: {self.status}
            {'='*50}
            Obrigado pela preferência!
            {'='*50}
            """
            print(recibo)
            return recibo
        else:
            print("Não é possível emitir recibo. Pagamento não aprovado.")
            return None


# ===== EXEMPLO DE USO =====
if __name__ == "__main__":
    # Criando cliente
    cliente1 = Cliente(
        identificacao="C001",
        nome="João Silva",
        cpf="123.456.789-00",
        email="joao@email.com",
        telefone="(67) 98765-4321"
    )
    cliente1.cadastrar()
    
    # Criando produtos
    produto1 = Produto(
        codigo="P001",
        nome="Notebook Dell",
        descricao="Notebook i7, 16GB RAM, 512GB SSD",
        preco=3500.00,
        quantidade_estoque=10
    )
    
    produto2 = Produto(
        codigo="P002",
        nome="Mouse Logitech",
        descricao="Mouse sem fio",
        preco=80.00,
        quantidade_estoque=50
    )
    
    produto3 = Produto(
        codigo="P003",
        nome="Teclado Mecânico",
        descricao="Teclado mecânico RGB",
        preco=250.00,
        quantidade_estoque=30
    )
    
    # Exibindo informações de um produto
    produto1.exibir_informacoes()
    
    # Criando um pedido
    pedido1 = Pedido(
        identificador="PED001",
        data=date.today(),
        cliente=cliente1
    )
    
    # Adicionando produtos ao pedido
    print("\n" + "="*50)
    print("ADICIONANDO PRODUTOS AO PEDIDO")
    print("="*50)
    pedido1.adicionar_produto(produto1, 1)
    pedido1.adicionar_produto(produto2, 2)
    pedido1.adicionar_produto(produto3, 1)
    
    # Exibindo o pedido
    pedido1.exibir_pedido()
    
    # Criando e processando pagamento
    print("\n" + "="*50)
    print("PROCESSANDO PAGAMENTO")
    print("="*50)
    pagamento1 = Pagamento(
        codigo="PAG001",
        pedido=pedido1,
        forma_pagamento="Cartão de Crédito",
        valor_pago=pedido1.valor_total,
        data=date.today()
    )
    
    pagamento1.processar_pagamento()
    pagamento1.confirmar()
    pagamento1.emitir_recibo()
    
    # Consultando pedidos do cliente
    print("\n" + "="*50)
    print("CONSULTANDO PEDIDOS DO CLIENTE")
    print("="*50)
    cliente1.consultar_pedidos()