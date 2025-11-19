veiculo = []
usuarios = []
def cadastrar_usuario():
    while True:
        try:
            nome = input("Digite o nome completo: ")
            cpf = int(input("Digite o CPF (apenas números): "))
            telefone = int(input("Digite o telefone (apenas números): "))


            usuarios.append({
                "nome": nome,
                "cpf": cpf,
                "telefone": telefone,
                
            })

            continuar = input("Deseja cadastrar outra pessoa? (S/N): ").upper()
            if continuar != "S":
                break
        except ValueError:
            print("Erro: Certifique-se de inserir valores válidos.")

    return usuarios


def salvar_usuarios(usuarios):
    with open("cadastro.txt", "w", encoding="utf-8") as f:
        for usuario in usuarios:
            f.write(f"Nome: {usuario['nome']}, Idade: {usuario['idade']}, Sexo: {usuario['sexo']}, "
                    f"Endereço: {usuario['endereco']}, Cidade: {usuario['cidade']}, Estado: {usuario['estado']}\n")


def consultar_usuarios():
    try:
        with open("cadastro.txt", "r", encoding="utf-8") as f:
            print("Dados cadastrados:")
            print(f.read())
    except FileNotFoundError:
        print("Nenhum dado encontrado. Certifique-se de cadastrar usuários primeiro.")


def main():
    while True:
        print("\nMenu:")
        print("1. Cadastrar usuários")
        print("2. Consultar dados")
        print("3. Sair")

        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            usuarios = cadastrar_usuario()
            salvar_usuarios(usuarios)
        elif opcao == "2":
            consultar_usuarios()
        elif opcao == "3":
            print("Encerrando o programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
