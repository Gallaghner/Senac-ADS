def menu():
    print("\n===== MENU =====")
    print("1. Cadastrar Pessoa")
    print("2. Consultar Dados")
    print("3. Sair")
    print("================\n")

def cadastrar_pessoa():
    while True:
        try:
            nome = input("Nome: ").strip()
            idade = int(input("Idade: "))
            sexo = input("Sexo (M/F): ").strip().upper()
            if sexo not in ['M', 'F']:
                raise ValueError("Sexo inválido. Use 'M' ou 'F'.")
            cpf = input("CPF: ").strip()
            endereco = input("Endereço: ").strip()
            cidade = input("Cidade: ").strip()
            estado = input("Estado (sigla): ").strip().upper()

            pessoa = {
                'nome': nome,
                'idade': idade,
                'sexo': sexo,
                'cpf': cpf,
                'endereco': endereco,
                'cidade': cidade,
                'estado': estado
            }
            cadastro.append(pessoa)
            print("Cadastro realizado com sucesso!")

        except ValueError as ve:
            print(f"Erro: {ve}")
            continue

        novamente = input("Deseja cadastrar outra pessoa? (S/N): ").strip().upper()
        if novamente != 'S':
            break

def salvar_em_arquivo():
    with open("cadastro.txt", "w", encoding='utf-8') as arquivo:
        for pessoa in cadastro:
            linha = f"Nome: {pessoa['nome']}, Idade: {pessoa['idade']}, Sexo:{pessoa['sexo']}, "
            linha += f"Endereço: {pessoa['endereco']}, Cidade: {pessoa['cidade']}, Estado: {pessoa['estado']}\n"
            linha += "-" * 90 + "\n"
            arquivo.write(linha)
    print("Dados salvos no arquivo 'cadastro.txt'.")

def consultar_dados():
    if not cadastro:
        print("Nenhum cadastro disponível.")
        return

    print("\nCampos disponíveis para consulta: nome, idade, sexo, cpf, endereco, cidade, estado")
    campo = input("Qual campo deseja consultar? ").strip().lower()

    if campo not in ['nome', 'idade', 'sexo', 'cpf', 'endereco', 'cidade', 'estado']:
        print("Campo inválido.")
        return

    for idx, pessoa in enumerate(cadastro, 1):
        print(f"{idx}. {pessoa[campo]}")
    print()

# Lista principal de cadastros
cadastro = []

# Loop principal
while True:
    menu()
    opcao = input("Escolha uma opção: ").strip()

    if opcao == '1':
        cadastrar_pessoa()
    elif opcao == '2':
        consultar_dados()
    elif opcao == '3':
        salvar_em_arquivo()
        print("Encerrando o programa. Até logo!")
        break
    else:
        print("Opção inválida. Tente novamente.")
