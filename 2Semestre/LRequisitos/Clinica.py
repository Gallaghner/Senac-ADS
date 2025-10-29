from datetime import datetime, time, date

class Cliente:
    def __init__(self, nome, cpf, telefone, email, endereco):
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
        self.email = email
        self.endereco = endereco
        self.agendamentos = []
    
    def cadastrar(self):
        """Cadastra o cliente no sistema"""
        print(f"Cliente {self.nome} cadastrado com sucesso!")
        return True
    
    def atualizar_dados(self, email,telefone):
        """Atualiza os dados do cliente"""
        self.email = email
        self.telefone = telefone
        print(f"Dados do cliente {self.nome} atualizados!")

    
lista_clientes = []   
c1 = Cliente('Joao','5648','6798234832','joao@gmail.com','Rua 5')
lista_clientes.append(c1)
c1.cadastrar()
print(lista_clientes)

class Produto:
    def __init__(self,nome,cod,desc, preco,qtd):
        self.nome = nome
        self.cod = cod
        self.desc = desc
        self.preco = preco
        self.qtd = qtd

    def atualizar(self,nova_qtd):
        self.nova_qtd = nova_qtd
        print(f"Estoque atualizado. Nova quantidade: {self.qtd}.")

    def aplicar_desconto(self, percentual):
        preco_desc = self.preco - (self.preco * {percentual/100})
        return preco_desc

    def infos_loja(self):
        print(f"Código {self.cod} | Nome: {self.nome} | Descrição {self.desc} | Preco: {self.preco:.2f} | Quantidade: {self.qtd}")

class ItemPedido:
    def __init__(self,cod,produto,qtd,preco_un):
        self.cod = cod
        self.produto = produto
        self.qtd = qtd
        self.preco_un = preco_un
        self.subtotal = self.calcular_subtotal()

    def calcular_subtotal(self):
        """Calcula o subtotal do item"""
        self.subtotal = self.qtd * self.preco_un
        return self.subtotal

    def att_qtd(self,nova_qtd):
        """Atualiza a qtd do item"""
        self.qtd = nova_qtd
        self.calcular_subtotal()
        print(f"Quantidade de {self.produto} atualizada para {nova_qtd}")
        print(f"Novo subtotal: R$ {self.subtotal:.2f}")

    def exibir_informacoes(self):
        """Exibe informações do item"""
        infos = f"""
        Item: {self.produto}
        Código: {self.cod}
        Quantidade: {self.qtd}
        Preço unitário: R${self.preco_un}
        Subtotal: R$ {self.subtotal:.2f}
        """
        print(infos)
        return infos
         
class Pedido:
    def __init__(self,id,data,cliente):
        self.id = id
        self.data = data
        self.cliente = cliente
        self.valor_total = 0.0
        self.status = "Aberto"
        self.itens = []
        self.pagamento = None

