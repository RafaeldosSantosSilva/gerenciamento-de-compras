def gerenciar_compras():
    produtos = []
    
    while True:
        nome = input("Digite o nome do produto: ")
        
        while True:
            preco_input = input("Digite o preço do produto: R$ ").replace(',', '.')
            try:
                preco = float(preco_input)
                break  # Sai do loop se a conversão for bem-sucedida
            except ValueError:
                print("Preço inválido. Por favor, insira um número válido.")
        
        produtos.append((nome, preco))
        
        continuar = input("Deseja adicionar mais produtos? (s/n): ").strip().lower()
        if continuar != 's':
            break
    
    total_gasto = sum(preco for _, preco in produtos)
    produtos_acima_1000 = sum(1 for _, preco in produtos if preco > 1000)
    produto_mais_barato = min(produtos, key=lambda x: x[1])

    print("\nResumo da Compra:")
    print(f"Total gasto: R$ {total_gasto:.2f}")
    print(f"Quantidade de produtos acima de R$ 1000: {produtos_acima_1000}")
    print(f"Produto mais barato: {produto_mais_barato[0]} (R$ {produto_mais_barato[1]:.2f})")

# Executando o programa
gerenciar_compras()
