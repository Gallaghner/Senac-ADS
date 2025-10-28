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

    def infos(self):
        print(f"Nome do produto: {self.nome} | Preco: {self.preco:.2f} | Quantidade: {self.qtd}")
         

