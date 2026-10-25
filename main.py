print("=== SISTEMA DE PEDIDO, FRETE E NOTA FISCAL ===")

# 1. Identificação do Cliente com Validação
while True:
    nome_input = input("Digite o nome do cliente: ")
    nome_limpo = nome_input.strip().title()

    if nome_limpo.replace(" ", "").isalpha():
        break
    print("Erro: O nome deve conter apenas letras. Tente novamente.")

print(f"Cliente validado com sucesso: {nome_limpo}\n")

# 2. Seleção do Produto do Catálogo
print("--- CATÁLOGO DE PRODUTOS ---")
print("[1] Caixa de Brigadeiros Gourmet - R$ 45.00")
print("[2] Doce de Leite Artesanal      - R$ 30.00")
print("[3] Torta de Limão Inteira      - R$ 60.00")

while True:
    opcao_produto = input("Escolha o produto (1, 2 ou 3): ").strip()

    if opcao_produto == "1":
        nome_produto = "Caixa de Brigadeiros Gourmet"
        preco_unitario = 45.00
        break
    elif opcao_produto == "2":
        nome_produto = "Doce de Leite Artesanal"
        preco_unitario = 30.00
        break
    elif opcao_produto == "3":
        nome_produto = "Torta de Limão Inteira"
        preco_unitario = 60.00
        break
    else:
        print("Opção inválida! Escolha 1, 2 ou 3.")

# Quantidade do Produto
while True:
    qtd_input = input(f"Quantas unidades de '{nome_produto}' o cliente deseja? ")
    if qtd_input.isnumeric():
        quantidade = int(qtd_input)
        if quantidade > 0:
            break
    print("Erro: Digite uma quantidade válida (maior que zero).")

valor_produtos = preco_unitario * quantidade

# 3. Distância da Entrega com Validação de Número
while True:
    distancia_input = input("\nDigite a distância da entrega em km: ")

    if distancia_input.isnumeric():
        distancia = float(distancia_input)
        break
    print("Erro: Digite apenas números válidos para a distância. Tente novamente.")

# 4. Escolha do Veículo e Definição da Tarifa
print("\n--- TIPO DE VEÍCULO PARA ENTREGA ---")
print("[1] Moto (R$ 1.50 por km)")
print("[2] Carro (R$ 3.00 por km)")

while True:
    opcao_veiculo = input("Escolha o veículo (1 ou 2): ").strip()

    if opcao_veiculo == "1":
        veiculo = "Moto"
        tarifa_km = 1.50
        break
    elif opcao_veiculo == "2":
        veiculo = "Carro"
        tarifa_km = 3.00
        break
    else:
        print("Opção inválida! Digite apenas 1 para Moto ou 2 para Carro.")

# 5. Cálculos de Frete e Taxas
valor_frete_base = distancia * tarifa_km

taxa_rodovia = 0.0
if distancia > 20:
    taxa_rodovia = 10.00
    print("-> Aviso: Distância superior a 20 km. Taxa de rodovia aplicada (+R$ 10.00).")

valor_frete_total = valor_frete_base + taxa_rodovia
valor_geral_pedido = valor_produtos + valor_frete_total

# 6. A Nota Fiscal / Recibo Final Completo
print("\n" + "=" * 50)
print("             NOTA FISCAL / RECIBO DE PEDIDO")
print("=" * 50)
print(f"Cliente:                 {nome_limpo}")
print(f"Produto:                 {quantidade}x {nome_produto}")
print(f"Subtotal Produtos:       R$ {valor_produtos:.2f}")
print("-" * 50)
print(f"Distância da Entrega:    {distancia} km ({veiculo})")
print(f"Valor do Frete:          R$ {valor_frete_total:.2f}")
if taxa_rodovia > 0:
    print(f"  (Inclui taxa de rodovia: R$ {taxa_rodovia:.2f})")
print("=" * 50)
print(f"VALOR TOTAL DO PEDIDO:   R$ {valor_geral_pedido:.2f}")
print("=" * 50)
print("         Obrigado pela preferência!           ")
print("=" * 50)