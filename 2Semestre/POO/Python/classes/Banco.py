import datetime

class Conta:
    """
    Representa uma conta bancária de um cliente.
    Armazena dados do titular, saldo, senha e histórico de transações.
    """
    def __init__(self, numero, nome_titular, senha, agencia="0001"):
        self.numero = numero
        self.agencia = agencia
        self.titular = nome_titular
        self.senha = senha
        self.saldo = 0.0
        self.historico = []

    def autenticar(self, senha_tentativa):
        """Verifica se a senha fornecida é a correta."""
        return self.senha == senha_tentativa

    def depositar(self, valor):
        """Adiciona um valor ao saldo da conta."""
        if valor > 0:
            self.saldo += valor
            self.historico.append(f"[{datetime.datetime.now():%d/%m/%Y %H:%M}] Depósito: +R$ {valor:.2f}")
            print("\n✅ Depósito realizado com sucesso!")
            return True
        print("\n❌ Valor de depósito inválido.")
        return False

    def sacar(self, valor):
        """Retira um valor do saldo da conta, se houver fundos."""
        if valor <= 0:
            print("\n❌ Valor de saque inválido.")
            return False
        if self.saldo < valor:
            print("\n❌ Saldo insuficiente.")
            return False
        
        self.saldo -= valor
        self.historico.append(f"[{datetime.datetime.now():%d/%m/%Y %H:%M}] Saque:    -R$ {valor:.2f}")
        print("\n✅ Saque realizado com sucesso!")
        return True

    def exibir_extrato(self):
        """Mostra o histórico de transações e o saldo final."""
        print("\n================ EXTRATO ================")
        if not self.historico:
            print("Não foram realizadas movimentações.")
        else:
            for transacao in self.historico:
                print(transacao)
        print(f"\nSaldo atual: R$ {self.saldo:.2f}")
        print("=======================================")

def buscar_conta(numero_conta, agencia, lista_contas):
    """Encontra uma conta na lista a partir do número e agência."""
    for conta in lista_contas:
        if conta.numero == numero_conta and conta.agencia == agencia:
            return conta
    return None

def main():
    """Função principal que executa o sistema bancário."""
    contas = []
    numero_proxima_conta = 1
    AGENCIA_PADRAO = "0001"

    while True:
        menu = """
================ MENU ================
[1] Criar Nova Conta
[2] Acessar Conta
[0] Sair
=> """
        opcao = input(menu)

        if opcao == '1':
            nome = input("Digite o nome completo do titular: ")
            senha = input("Crie uma senha para a conta: ")
            
            nova_conta = Conta(numero=numero_proxima_conta, nome_titular=nome, senha=senha, agencia=AGENCIA_PADRAO)
            contas.append(nova_conta)
            
            print(f"\n✅ Conta criada com sucesso! Anote seus dados:")
            print(f"   Agência: {nova_conta.agencia}")
            print(f"   Conta:   {nova_conta.numero}")
            numero_proxima_conta += 1

        elif opcao == '2':
            try:
                numero_input = int(input("Digite o número da conta: "))
            except ValueError:
                print("\n❌ Número da conta inválido. Use apenas números.")
                continue

            conta = buscar_conta(numero_input, AGENCIA_PADRAO, contas)

            if not conta:
                print("\n❌ Conta não encontrada.")
                continue

            senha_tentativa = input("Digite a senha: ")
            if not conta.autenticar(senha_tentativa):
                print("\n❌ Senha incorreta.")
                continue
            
            print(f"\n✅ Acesso liberado! Olá, {conta.titular}.")
            
            while True:
                op_menu = "\n-- Operações --\n[d] Depositar\n[s] Sacar\n[e] Extrato\n[c] Saldo\n[q] Sair da conta\n=> "
                operacao = input(op_menu).lower()

                if operacao == 'd':
                    valor = float(input("Digite o valor para depósito: R$ "))
                    conta.depositar(valor)
                elif operacao == 's':
                    valor = float(input("Digite o valor para saque: R$ "))
                    conta.sacar(valor)
                elif operacao == 'c':
                     print(f"\n-- Saldo Atual --\n R$ {conta.saldo:.2f}")
                elif operacao == 'e':
                    conta.exibir_extrato()
                elif operacao == 'q':
                    print("\nSaindo da conta...")
                    break
                else:
                    print("\n❌ Opção inválida.")

        elif opcao == '0':
            print("\nObrigado por usar nosso sistema. Até logo! 👋")
            break
        
        else:
            print("\n❌ Opção inválida. Por favor, tente novamente.")

if __name__ == "__main__":
    main()