from Produto import Produto
from Garcom import Garcom

# Função principal para organizar o teste
def main():
    print("--- INICIANDO SISTEMA ---\n")

    # 1. Criando Produtos (Preço deve ser número, sem aspas)
    p1 = Produto("Pizza Calabresa", 40.00, "Massas", "Grande")
    p2 = Produto("Coca-Cola", 8.00, "Bebidas", "2 Litros")
    p3 = Produto("Pudim", 12.00, "Sobremesa", "Leite condensado")

    # 2. Criando Garçom
    g1 = Garcom(1, "João Pedro")
    print(g1) # Testa o __str__ do garçom

    # 3. Garçom registra o pedido (passando ID e lista de produtos)
    print("\n> Registrando pedido...")
    pedido_mesa = g1.registrar_pedido(101, [p1, p2])

    # 4. Exibindo resumo inicial
    print("\n> Resumo Inicial:")
    pedido_mesa.resumo_pedido()

    # 5. Adicionando mais um item (Pudim)
    print("\n> Cliente pediu sobremesa...")
    pedido_mesa.adicionar_produto(p3)
    
    # 6. Alterando status
    pedido_mesa.alterar_status("Na Cozinha")

    # 7. Resumo Final
    print("\n> Resumo Final:")
    pedido_mesa.resumo_pedido()

# Proteção para rodar apenas se for o arquivo principal
if __name__ == "__main__":
    main()