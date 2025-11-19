# Projeto Fábio e João Pedro Rodrigues


import os
import re

# ------------------ Validações ------------------

def validar_cpf(cpf):
    cpf = re.sub(r'\D', '', cpf)
    if len(cpf) != 11 or cpf == cpf[0] * 11:
        return False, "CPF deve ter 11 dígitos únicos."
    return True, cpf

def validar_telefone(tel):
    tel = re.sub(r'\D', '', tel)
    if len(tel) < 10 or len(tel) > 11:
        return False, "Telefone deve ter 10 ou 11 dígitos."
    return True, tel

def validar_placa(placa):
    placa = placa.upper().strip()
    if not re.match(r'^[A-Z]{3}[-]?\d{4}$|^[A-Z]{3}\d[A-Z]\d{2}$', placa):
        return False, "Formato inválido. Use: ABC1234 ou ABC1A23"
    return True, placa

def validar_valor(valor):
    try:
        val = float(valor.replace(',', '.'))
        return val >= 0, f"{val:.2f}" if val >= 0 else "Valor não pode ser negativo."
    except:
        return False, "Valor inválido."

def input_validado(prompt, validador, max_tent=3):
    for i in range(max_tent):
        entrada = input(prompt).strip()
        if entrada.lower() == 'sair':
            return None
        valido, resultado = validador(entrada)
        if valido:
            return resultado
        print(f"❌ {resultado} ({i+1}/{max_tent})")
    print("❌ Muitas tentativas. Operação cancelada.")
    return None

# ------------------ Funções auxiliares ------------------

def criar_arquivo(nome):
    if not os.path.exists(nome):
        open(nome, 'w').close()

def buscar_por_campo(arquivo, campo_idx, valor):
    try:
        with open(arquivo, 'r') as f:
            for linha in f:
                if linha.strip():
                    campos = linha.strip().split(';')
                    if len(campos) > campo_idx and campos[campo_idx] == valor:
                        return campos
    except FileNotFoundError:
        pass
    return None

def listar_arquivo(arquivo, cabecalho, formato):
    try:
        with open(arquivo, 'r') as f:
            linhas = [l.strip() for l in f if l.strip()]
        if not linhas:
            print("Nenhum registro encontrado.")
            return
        print(f"\n{cabecalho}")
        print("-" * 60)
        for linha in linhas:
            campos = linha.split(';')
            if len(campos) >= len(formato):
                print(formato.format(*campos))
    except FileNotFoundError:
        print("❌ Arquivo não encontrado.")

def atualizar_linha(arquivo, chave_idx, chave, nova_linha):
    try:
        linhas = []
        with open(arquivo, 'r') as f:
            for linha in f:
                if linha.strip():
                    if linha.strip().split(';')[chave_idx] != chave:
                        linhas.append(linha.strip())
        linhas.append(nova_linha)
        with open(arquivo, 'w') as f:
            for linha in linhas:
                f.write(linha + '\n')
        return True
    except:
        return False

def remover_linhas(arquivo, campo_idx, valor):
    try:
        linhas = []
        with open(arquivo, 'r') as f:
            for linha in f:
                if linha.strip():
                    campos = linha.strip().split(';')
                    if len(campos) <= campo_idx or campos[campo_idx] != valor:
                        linhas.append(linha.strip())
        with open(arquivo, 'w') as f:
            for linha in linhas:
                f.write(linha + '\n')
        return True
    except:
        return False

# ------------------ Cadastros ------------------

def cadastrar_cliente():
    print("\n=== CADASTRAR CLIENTE ===")
    cpf = input_validado("CPF: ", validar_cpf)
    if not cpf or buscar_por_campo('clientes.txt', 0, cpf):
        print("❌ CPF inválido ou já cadastrado.")
        return
    
    nome = input("Nome: ").strip().title()
    if not nome:
        print("❌ Nome obrigatório.")
        return
    
    telefone = input_validado("Telefone: ", validar_telefone)
    if not telefone:
        return
    
    with open('clientes.txt', 'a') as f:
        f.write(f"{cpf};{nome};{telefone}\n")
    print("✅ Cliente cadastrado!")

def cadastrar_veiculo():
    print("\n=== CADASTRAR VEÍCULO ===")
    cpf = input_validado("CPF do proprietário: ", validar_cpf)
    if not cpf or not buscar_por_campo('clientes.txt', 0, cpf):
        print("❌ Cliente não encontrado.")
        return
    
    placa = input_validado("Placa: ", validar_placa)
    if not placa or buscar_por_campo('veiculos.txt', 0, placa):
        print("❌ Placa inválida ou já cadastrada.")
        return
    
    modelo = input("Modelo: ").strip().title()
    ano = input("Ano: ").strip()
    
    if not modelo or not ano.isdigit() or not (1900 <= int(ano) <= 2030):
        print("❌ Modelo/ano inválido.")
        return
    
    with open('veiculos.txt', 'a') as f:
        f.write(f"{placa};{modelo};{ano};{cpf}\n")
    print("✅ Veículo cadastrado!")

def cadastrar_os():
    print("\n=== CADASTRAR OS ===")
    numero = input("Número da OS: ").strip()
    if not numero or buscar_por_campo('ordens_servico.txt', 0, numero):
        print("❌ Número inválido ou OS já existe.")
        return
    
    cpf = input_validado("CPF do cliente: ", validar_cpf)
    if not cpf or not buscar_por_campo('clientes.txt', 0, cpf):
        print("❌ Cliente não encontrado.")
        return
    
    placa = input_validado("Placa: ", validar_placa)
    veiculo = buscar_por_campo('veiculos.txt', 0, placa)
    if not veiculo or veiculo[3] != cpf:
        print("❌ Veículo não encontrado ou não pertence ao cliente.")
        return
    
    descricao = input("Descrição: ").strip()
    valor = input_validado("Valor: R$ ", validar_valor)
    
    if not descricao or not valor:
        print("❌ Descrição/valor obrigatório.")
        return
    
    with open('ordens_servico.txt', 'a') as f:
        f.write(f"{numero};{descricao};{valor};{cpf};{placa}\n")
    print("✅ OS cadastrada!")

# ------------------ Listagens ------------------

def listar_clientes():
    listar_arquivo('clientes.txt', 
                  "=== CLIENTES ===",
                  "{:<12} {:<25} {:<12}")

def listar_veiculos():
    listar_arquivo('veiculos.txt',
                  "=== VEÍCULOS ===", 
                  "{:<10} {:<20} {:<6} {:<12}")

def listar_os():
    listar_arquivo('ordens_servico.txt',
                  "=== ORDENS DE SERVIÇO ===",
                  "{:<8} {:<20} R${:<8} {:<12} {:<10}")

# ------------------ Consultas ------------------

def consultar_veiculos_cpf():
    cpf = input_validado("CPF: ", validar_cpf)
    if not cpf:
        return
    
    print(f"\n=== VEÍCULOS DO CPF {cpf} ===")
    encontrou = False
    try:
        with open('veiculos.txt', 'r') as f:
            for linha in f:
                if linha.strip():
                    campos = linha.strip().split(';')
                    if len(campos) >= 4 and campos[3] == cpf:
                        print(f"{campos[0]:<10} {campos[1]:<20} {campos[2]}")
                        encontrou = True
    except FileNotFoundError:
        pass
    
    if not encontrou:
        print("❌ Nenhum veículo encontrado.")

def consultar_os():
    print("1. Por CPF  2. Por número")
    op = input("Opção: ")
    
    if op == '1':
        cpf = input_validado("CPF: ", validar_cpf)
        if not cpf:
            return
        print(f"\n=== OS DO CPF {cpf} ===")
        try:
            with open('ordens_servico.txt', 'r') as f:
                for linha in f:
                    if linha.strip():
                        campos = linha.strip().split(';')
                        if len(campos) >= 5 and campos[3] == cpf:
                            print(f"OS: {campos[0]} | R$ {campos[2]} | {campos[1]}")
        except FileNotFoundError:
            print("❌ Arquivo não encontrado.")
    
    elif op == '2':
        numero = input("Número da OS: ").strip()
        os = buscar_por_campo('ordens_servico.txt', 0, numero)
        if os:
            print(f"\nOS: {os[0]}\nDescrição: {os[1]}\nValor: R$ {os[2]}\nCPF: {os[3]}\nPlaca: {os[4]}")
        else:
            print("❌ OS não encontrada.")

# ------------------ Edições ------------------

def editar_cliente():
    cpf = input_validado("CPF a editar: ", validar_cpf)
    if not cpf:
        return
    
    cliente = buscar_por_campo('clientes.txt', 0, cpf)
    if not cliente:
        print("❌ Cliente não encontrado.")
        return
    
    print(f"Atual: {cliente[1]} | {cliente[2]}")
    nome = input("Novo nome (Enter=manter): ").strip().title() or cliente[1]
    tel = input("Novo telefone (Enter=manter): ").strip()
    
    if tel:
        valido, tel = validar_telefone(tel)
        if not valido:
            print(f"❌ {tel}")
            return
    else:
        tel = cliente[2]
    
    if atualizar_linha('clientes.txt', 0, cpf, f"{cpf};{nome};{tel}"):
        print("✅ Cliente atualizado!")

def editar_veiculo():
    placa = input_validado("Placa a editar: ", validar_placa)
    if not placa:
        return
    
    veiculo = buscar_por_campo('veiculos.txt', 0, placa)
    if not veiculo:
        print("❌ Veículo não encontrado.")
        return
    
    print(f"Atual: {veiculo[1]} | {veiculo[2]}")
    modelo = input("Novo modelo (Enter=manter): ").strip().title() or veiculo[1]
    ano = input("Novo ano (Enter=manter): ").strip() or veiculo[2]
    
    if atualizar_linha('veiculos.txt', 0, placa, f"{placa};{modelo};{ano};{veiculo[3]}"):
        print("✅ Veículo atualizado!")

def editar_os():
    numero = input("Número da OS: ").strip()
    os = buscar_por_campo('ordens_servico.txt', 0, numero)
    if not os:
        print("❌ OS não encontrada.")
        return
    
    print(f"Atual: {os[1]} | R$ {os[2]}")
    desc = input("Nova descrição (Enter=manter): ").strip() or os[1]
    val = input("Novo valor (Enter=manter): ").strip()
    
    if val:
        valido, val = validar_valor(val)
        if not valido:
            print(f"❌ {val}")
            return
    else:
        val = os[2]
    
    if atualizar_linha('ordens_servico.txt', 0, numero, f"{numero};{desc};{val};{os[3]};{os[4]}"):
        print("✅ OS atualizada!")

# ------------------ Exclusões ------------------

def excluir_cliente():
    cpf = input_validado("CPF a excluir: ", validar_cpf)
    if not cpf or not buscar_por_campo('clientes.txt', 0, cpf):
        print("❌ Cliente não encontrado.")
        return
    
    if input("⚠️ Confirmar exclusão? (CONFIRMAR): ") == "CONFIRMAR":
        if (remover_linhas('clientes.txt', 0, cpf) and
            remover_linhas('veiculos.txt', 3, cpf) and
            remover_linhas('ordens_servico.txt', 3, cpf)):
            print("✅ Cliente excluído!")

def excluir_veiculo():
    placa = input_validado("Placa a excluir: ", validar_placa)
    if not placa or not buscar_por_campo('veiculos.txt', 0, placa):
        print("❌ Veículo não encontrado.")
        return
    
    if input("Confirmar exclusão? (s/N): ").lower() == 's':
        if (remover_linhas('veiculos.txt', 0, placa) and
            remover_linhas('ordens_servico.txt', 4, placa)):
            print("✅ Veículo excluído!")

def excluir_os():
    numero = input("Número da OS: ").strip()
    if not numero or not buscar_por_campo('ordens_servico.txt', 0, numero):
        print("❌ OS não encontrada.")
        return
    
    if input("Confirmar exclusão? (s/N): ").lower() == 's':
        if remover_linhas('ordens_servico.txt', 0, numero):
            print("✅ OS excluída!")

# ------------------ Menu ------------------

def menu():
    for arquivo in ['clientes.txt', 'veiculos.txt', 'ordens_servico.txt']:
        criar_arquivo(arquivo)
    
    opcoes = {
        '1': cadastrar_cliente, '2': cadastrar_veiculo, '3': cadastrar_os,
        '4': listar_clientes, '5': listar_veiculos, '6': listar_os,
        '7': consultar_veiculos_cpf, '8': consultar_os,
        '9': editar_cliente, '10': editar_veiculo, '11': editar_os,
        '12': excluir_cliente, '13': excluir_veiculo, '14': excluir_os
    }
    
    while True:
        print("\n" + "="*40)
        print("  🔧 SISTEMA OFICINA MECÂNICA")
        print("="*40)
        menu_items = [
            "1. Cadastrar Cliente", "2. Cadastrar Veículo", "3. Cadastrar OS",
            "4. Listar Clientes", "5. Listar Veículos", "6. Listar OS",
            "7. Consultar Veículos/CPF", "8. Consultar OS",
            "9. Editar Cliente", "10. Editar Veículo", "11. Editar OS",
            "12. Excluir Cliente", "13. Excluir Veículo", "14. Excluir OS",
            "0. Sair"
        ]
        
        for item in menu_items:
            print(item)
        
        try:
            opcao = input("\nEscolha: ").strip()
            if opcao == '0':
                print("👋 Até logo!")
                break
            elif opcao in opcoes:
                opcoes[opcao]()
                input("\nPressione Enter...")
            else:
                print("❌ Opção inválida!")
        except KeyboardInterrupt:
            print("\n👋 Sistema encerrado!")
            break
        except Exception as e:
            print(f"❌ Erro: {e}")

if __name__ == "__main__":
    menu()