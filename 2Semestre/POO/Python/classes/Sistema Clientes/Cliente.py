# Cliente.py - Corrigido
from Database import Database

class Cliente:
    def __init__(self,nome=None,cpf=None,fone=None,cidade=None):
        self.nome = nome
        self.cpf = cpf
        self.fone = fone
        self.cidade = cidade

    def cadastrar(self):
        self.db = Database()
        tupla = (self.nome,self.cpf,self.fone,self.cidade)
        result = self.db.insert(tupla)
        return result

    def buscar(self):
        self.db = Database()
        dados = self.db.select()
        return dados

    def atualizar(self,tupla):
        self.db = Database()
        dados = self.db.update(tupla)
        return dados

    def buscar_por_id(self,id):
        self.db = Database()
        cliente = self.db.select_by_id(id)
        return cliente

    def excluir(self,id):
        self.db = Database()
        result = self.db.delete(id)
        return result

# CORREÇÃO: O código abaixo foi movido para dentro deste bloco
if __name__ == "__main__":
    print("--- Este é um teste do módulo Cliente ---")
    cli = Cliente()
    clientes = cli.buscar()

    for item in clientes:
        print(item)

    # O resto do seu código de teste pode ficar aqui.
    # id_atualizar = int(input("Digite o id do cliente para atualizar"))
    # ...