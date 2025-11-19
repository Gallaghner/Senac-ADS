# main.py - Corrigido
from Cliente import Cliente

while True:
    print("\nSysPerkal") # Adicionei um \n para melhorar a visualização
    print("*"*30)
    print("Selecione uma opção")
    opcao = input("1 - Cadastrar \n2 - Listar Clientes \n3 - Excluir Cliente \n4 - Atualizar \n0 - SAIR\n")

    if opcao == "0":
        break
    elif opcao == "1":
        cli = Cliente()
        cli.nome = input("Digite o nome do cliente: ")
        cli.cpf = input("Digite o CPF: ")
        cli.fone = input("Digite o telefone: ")
        cli.cidade = input("Digite sua cidade: ")
        result = cli.cadastrar()
        if result == True:
            print("Cadastrado com sucesso!")
        else:
            print("Erro ao cadastrar.") # Adicionado feedback de erro

    elif opcao == "2":
        cli = Cliente()
        result = cli.buscar()
        for cliente in result:
            print(f'ID: {cliente[0]} | NOME: {cliente[1]} | CPF: {cliente[2]} | FONE: {cliente[3]} | CIDADE: {cliente[4]}')

    elif opcao == "3":
        cli = Cliente()
        result = cli.buscar()
        for cliente in result:
            print(f'ID: {cliente[0]} | NOME: {cliente[1]} | CPF: {cliente[2]} | FONE: {cliente[3]} | CIDADE: {cliente[4]}')

        try: # Adicionado para evitar erro se o usuário não digitar um número
            id_excluir = int(input("Digite o ID que deseja excluir: "))
            result = cli.excluir(id_excluir)
            if result == True:
                print("Excluído(a) com sucesso!")
            else:
                print("Erro ao excluir.") # Adicionado feedback de erro
        except ValueError:
            print("ID inválido. Por favor, digite um número.")


    elif opcao == "4":
        cli = Cliente()
        result = cli.buscar()
        for cliente in result:
            print(f'ID: {cliente[0]} | NOME: {cliente[1]} | CPF: {cliente[2]} | FONE: {cliente[3]} | CIDADE: {cliente[4]}')

        try: # Adicionado para evitar erro se o usuário não digitar um número
            id_atualiza = int(input("Digite o ID a ser atualizado:"))
            result = cli.buscar_por_id(id_atualiza)

            if result: # Verifica se o cliente foi encontrado
                result = list(result)
                result[1] = input("Digite novo Nome: ")
                result[2] = input("Digite novo CPF: ")
                result[3] = input("Digite novo telefone: ")
                result[4] = input("Digite nova cidade: ")

                # >>>>> CORREÇÃO PRINCIPAL AQUI <<<<<
                
                atualizacao = cli.atualizar(tuple(result))

                if atualizacao == True:
                    print("Cliente atualizado com sucesso!")
                else:
                    print("Erro ao atualizar.") # Adicionado feedback de erro
            else:
                print("Cliente não encontrado com o ID informado.")
        except ValueError:
            print("ID inválido. Por favor, digite um número.")

    else:
        print("Opção inválida!")