import os

# ------------------ Funções auxiliares ------------------

def verificar_existencia(caminho_arquivo):
    if not os.path.exists(caminho_arquivo):
        with open(caminho_arquivo, 'w') as f:
            pass  # Cria arquivo vazio

def buscar_cliente_por_cpf(cpf):
    with open('clientes.txt', 'r') as f:
        for linha in f:
            campos = linha.strip().split(';')
            if campos[0] == cpf:
                return campos
    return None

def buscar_veiculo_por_placa(placa):
    with open('veiculos.txt', 'r') as f:
        for linha in f:
            campos = linha.strip().split(';')
            if campos[0] == placa:
                return campos
    return None

def buscar_os_por_numero(numero_os):
    with open('ordens_servico.txt', 'r') as f:
        for linha in f:
            campos = linha.strip().split(';')
            if campos[0] == numero_os:
                return campos
    return None
	
# ------------------ Cadastro ------------------

def cadastrar_cliente():
    cpf = input("CPF: ").strip()
    if buscar_cliente_por_cpf(cpf):
        print("Cliente já cadastrado.")
        return
    nome = input("Nome completo: ").strip()
    telefone = input("Telefone: ").strip()		
    with open('clientes.txt', 'a') as f:
        f.write(f"{cpf};{nome};{telefone}\n")
    print("Cliente cadastrado com sucesso.")

def cadastrar_veiculo():
    cpf = input("CPF do proprietário: ").strip()
    if not buscar_cliente_por_cpf(cpf):
        print("Cliente não encontrado.")
        return
    placa = input("Placa do veículo: ").strip()
    if buscar_veiculo_por_placa(placa):
        print("Veículo já cadastrado.")
        return
    modelo = input("Modelo: ").strip()
    ano = input("Ano: ").strip()
    with open('veiculos.txt', 'a') as f:
        f.write(f"{placa};{modelo};{ano};{cpf}\n")
    print("Veículo cadastrado com sucesso.")

def cadastrar_ordem_servico():
    numero = input("Número da OS: ").strip()
    if buscar_os_por_numero(numero):
        print("OS já cadastrada.")
        return
    cpf = input("CPF do cliente: ").strip()
    if not buscar_cliente_por_cpf(cpf):
        print("Cliente não encontrado.")
        return
    placa = input("Placa do veículo: ").strip()
    if not buscar_veiculo_por_placa(placa):
        print("Veículo não encontrado.")
        return
    descricao = input("Descrição do serviço: ").strip()
    valor = input("Valor: ").strip()
    with open('ordens_servico.txt', 'a') as f:
        f.write(f"{numero};{descricao};{valor};{cpf};{placa}\n")
    print("Ordem de serviço cadastrada com sucesso.")

# ------------------ Listagens e Consultas ------------------

def listar_clientes():
    try:
        with open('clientes.txt', 'r') as f:
            print("\n--- Lista de Clientes ---")
            for linha in f:
                print(linha.strip())
    except FileNotFoundError:
        print("Arquivo clientes.txt não encontrado.")

def listar_veiculos():
    try:
        with open('veiculos.txt', 'r') as f:
            print("\n--- Lista de Veículos ---")
            for linha in f:
                print(linha.strip())
    except FileNotFoundError:
        print("Arquivo veiculos.txt não encontrado.")

def listar_os():
    try:
        with open('ordens_servico.txt', 'r') as f:
            print("\n--- Lista de Ordens de Serviço ---")
            for linha in f:
                print(linha.strip())
    except FileNotFoundError:
        print("Arquivo ordens_servico.txt não encontrado.")

def consultar_veiculos_por_cpf():
    cpf = input("Digite o CPF: ").strip()
    encontrados = []
    with open('veiculos.txt', 'r') as f:
        for linha in f:
            if linha.strip().split(';')[3] == cpf:
                encontrados.append(linha.strip())
    if encontrados:
        print("\nVeículos encontrados:")
        for v in encontrados:
            print(v)
    else:
        print("Nenhum veículo encontrado para este CPF.")

def consultar_os():
    opcao = input("Consultar por (1) CPF ou (2) Número da OS? ")
    if opcao == '1':
        cpf = input("Digite o CPF: ").strip()
        with open('ordens_servico.txt', 'r') as f:
            for linha in f:
                if linha.strip().split(';')[3] == cpf:
                    print(linha.strip())
    elif opcao == '2':
        numero = input("Digite o número da OS: ").strip()
        os_encontrada = buscar_os_por_numero(numero)
        if os_encontrada:
            print(";".join(os_encontrada))
        else:
            print("Ordem de serviço não encontrada.")

# ------------------ Edição ------------------

def editar_cliente():
    cpf = input("CPF do cliente a editar: ").strip()
    cliente = buscar_cliente_por_cpf(cpf)
    if not cliente:
        print("Cliente não encontrado.")
        return
    nome = input("Novo nome (enter para manter): ").strip() or cliente[1]
    telefone = input("Novo telefone (enter para manter): ").strip() or cliente[2]
    atualizar_arquivo('clientes.txt', cpf, f"{cpf};{nome};{telefone}")
    print("Cliente atualizado.")

def editar_veiculo():
    placa = input("Placa do veículo a editar: ").strip()
    veiculo = buscar_veiculo_por_placa(placa)
    if not veiculo:
        print("Veículo não encontrado.")
        return
    modelo = input("Novo modelo (enter para manter): ").strip() or veiculo[1]
    ano = input("Novo ano (enter para manter): ").strip() or veiculo[2]
    atualizar_arquivo('veiculos.txt', placa, f"{placa};{modelo};{ano};{veiculo[3]}")
    print("Veículo atualizado.")

def editar_os():
    numero = input("Número da OS a editar: ").strip()
    os = buscar_os_por_numero(numero)
    if not os:
        print("OS não encontrada.")
        return
    descricao = input("Nova descrição (enter para manter): ").strip() or os[1]
    valor = input("Novo valor (enter para manter): ").strip() or os[2]
    atualizar_arquivo('ordens_servico.txt', numero, f"{numero};{descricao};{valor};{os[3]};{os[4]}")
    print("OS atualizada.")

# ------------------ Exclusão ------------------

def excluir_cliente():
    cpf = input("CPF do cliente a excluir: ").strip()
    if not buscar_cliente_por_cpf(cpf):
        print("Cliente não encontrado.")
        return
    remover_linha('clientes.txt', cpf)
    remover_linhas_por_campo('veiculos.txt', 3, cpf)
    remover_linhas_por_campo('ordens_servico.txt', 3, cpf)
    print("Cliente e seus dados removidos.")

def excluir_veiculo():
    placa = input("Placa do veículo a excluir: ").strip()
    if not buscar_veiculo_por_placa(placa):
        print("Veículo não encontrado.")
        return
    remover_linha('veiculos.txt', placa)
    remover_linhas_por_campo('ordens_servico.txt', 4, placa)
    print("Veículo e ordens relacionadas removidas.")

def excluir_os():
    numero = input("Número da OS a excluir: ").strip()
    if not buscar_os_por_numero(numero):
        print("OS não encontrada.")
        return
    remover_linha('ordens_servico.txt', numero)
    print("OS removida.")

# ------------------ Funções genéricas de manipulação ------------------

def atualizar_arquivo(nome_arquivo, chave, nova_linha):
    linhas = []
    with open(nome_arquivo, 'r') as f:
        for linha in f:
            if linha.strip().split(';')[0] != chave:
                linhas.append(linha.strip())
    linhas.append(nova_linha)
    with open(nome_arquivo, 'w') as f:
        for l in linhas:
            f.write(l + '\n')

def remover_linha(nome_arquivo, chave):
    linhas = []
    with open(nome_arquivo, 'r') as f:
        for linha in f:
            if linha.strip().split(';')[0] != chave:
                linhas.append(linha.strip())
    with open(nome_arquivo, 'w') as f:
        for l in linhas:
            f.write(l + '\n')

def remover_linhas_por_campo(nome_arquivo, indice, valor):
    linhas = []
    with open(nome_arquivo, 'r') as f:
        for linha in f:
            if linha.strip().split(';')[indice] != valor:
                linhas.append(linha.strip())
    with open(nome_arquivo, 'w') as f:
        for l in linhas:
            f.write(l + '\n')

# ------------------ Menu Interativo ------------------

def menu():
    for arquivo in ['clientes.txt', 'veiculos.txt', 'ordens_servico.txt']:
        verificar_existencia(arquivo)

    while True:
        print("\n--- MENU PRINCIPAL ---")
        print("1. Cadastrar Cliente")
        print("2. Cadastrar Veículo")
        print("3. Cadastrar Ordem de Serviço")
        print("4. Listar Clientes")
        print("5. Listar Veículos")
        print("6. Listar Ordens de Serviço")
        print("7. Consultar Veículos por CPF")
        print("8. Consultar OS por CPF ou número")
        print("9. Editar Cliente")
        print("10. Editar Veículo")
        print("11. Editar OS")
        print("12. Excluir Cliente")
        print("13. Excluir Veículo")
        print("14. Excluir OS")
        print("0. Sair")

        opcao = input("Escolha uma opção: ")
        try:
            match opcao:
                case '1': cadastrar_cliente()
                case '2': cadastrar_veiculo()
                case '3': cadastrar_ordem_servico()
                case '4': listar_clientes()
                case '5': listar_veiculos()
                case '6': listar_os()
                case '7': consultar_veiculos_por_cpf()
                case '8': consultar_os()
                case '9': editar_cliente()
                case '10': editar_veiculo()
                case '11': editar_os()
                case '12': excluir_cliente()
                case '13': excluir_veiculo()
                case '14': excluir_os()
                case '0':
                    print("Saindo...")
                    break
                case _:
                    print("Opção inválida.")
        except Exception as e:
            print(f"Erro: {e}")

# ------------------ Execução ------------------

if __name__ == "__main__":
    menu()