nome = input("Digite o seu nome completo: ")
cpf = input("Digite o número do seu CPF: ")
rg = input("Digite o número do seu RG: ")
tel = input("Digite o número do seu telefone: ")
agencia = input("Digite o número da sua agência: ")
conta = (input("Digite o número da sua conta: "))
sinicial= int(input("Digite o valor do seu saldo inicial (valor em reais): "))

cliente1= [nome, cpf, rg, tel, agencia, conta, sinicial]
clientes = [""]
clientes.append(cliente1)

print("Nome: ", nome)
print("CPF: ", cpf)
print("RG: ", rg)
print("Telefone: ", tel)
print("Agência: ", agencia)
print("Conta: ", conta)
print("Saldo inicial: ", sinicial)

while True:
    print("Opções: ")
    print("1 - Ver saldo")
    print("2 - Depositar")
    print("3 - Sacar")
    print("4 - Sair")

    opcao = int(input("Digite a opção desejada: "))

    if opcao == 1:
        print("Saldo: ", sinicial)
    elif opcao == 2:
        d = int(input("Digite o valor a ser depositado: "))
        satual = sinicial + d
        print("Saldo após depósito: R$", satual)
    elif opcao == 3:
        s = int(input("Digite o valor que deseja sacar: "))
        satual = sinicial - s
        print("O saldo após o saque é de: R$", satual)
    else:
        print("Menu inicial")
        break
