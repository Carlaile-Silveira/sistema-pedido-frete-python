
# BANCO DE DADOS TEMPORÁRIO (SIMULAÇÃO DE BD)

# Simula a tabela 'clientes' do MySQL
banco_clientes = []

# Simula a tabela 'produtos' com o estoque do MySQL
banco_produtos = [
    {"id": 1, "nome": "Caixa de Brigadeiros Gourmet", "preco": 45.00, "estoque": 10},
    {"id": 2, "nome": "Doce de Leite Artesanal", "preco": 30.00, "estoque": 15},
    {"id": 3, "nome": "Torta de Limão Inteira", "preco": 60.00, "estoque": 5}
]

cliente_logado = None


# LOOP PRINCIPAL DA APLICAÇÃO

while True:
    print("\n" + "=" * 50)
    print("        SISTEMA DE LOJA - PEDIDO E FRETE")
    print("=" * 50)

    if not cliente_logado:
        print("[1] Cadastrar Cliente")
        print("[2] Fazer Login")
        print("[0] Sair")
    else:
        print(f"Sessão ativa: Cliente {cliente_logado['nome']}")
        print("[1] Realizar Novo Pedido")
        print("[2] Consultar Estoque de Produtos")
        print("[3] Fazer Logout")
        print("[0] Sair")

    opcao_menu = input("\nEscolha uma opção: ").strip()


    # OPÇÃO DE CADASTRO (Quando não há cliente logado)

    if opcao_menu == "1" and not cliente_logado:
        print("\n--- CADASTRO DE CLIENTE ---")
        while True:
            nome_input = input("Digite o nome completo do cliente: ").strip()
            if nome_input.replace(" ", "").isalpha() and len(nome_input) > 0:
                nome_limpo = nome_input.title()
                break
            print("Erro: O nome deve conter apenas letras. Tente novamente.")

        email_input = input("Digite o e-mail: ").strip().lower()
        senha_input = input("Digite a senha: ").strip()

        # Guarda o cliente na nossa 'tabela' simulada
        novo_cliente = {
            "id": len(banco_clientes) + 1,
            "nome": nome_limpo,
            "email": email_input,
            "senha": senha_input
        }
        banco_clientes.append(novo_cliente)
        print(f"\n✅ Cliente '{nome_limpo}' cadastrado com sucesso!")


    # OPÇÃO DE LOGIN (Quando não há cliente logado)

    elif opcao_menu == "2" and not cliente_logado:
        print("\n--- LOGIN DE CLIENTE ---")
        email_login = input("E-mail: ").strip().lower()
        senha_login = input("Senha: ").strip()

        # Procura o cliente cadastrado na lista
        sucesso_login = False
        for cliente in banco_clientes:
            if cliente["email"] == email_login and cliente["senha"] == senha_login:
                cliente_logado = cliente
                sucesso_login = True
                print(f"\n✅ Bem-vindo(a) de volta, {cliente_logado['nome']}!")
                break

        if not sucesso_login:
            print("\n❌ Erro: E-mail ou senha incorretos! (Cadastre-se primeiro se for novo cliente).")


    # REALIZAR PEDIDO (Quando o cliente ESTÁ LOGADO)

    elif opcao_menu == "1" and cliente_logado:
        print(f"\n=== REALIZANDO PEDIDO PARA: {cliente_logado['nome']} ===")

        # Seleção do Produto
        print("\n--- CATÁLOGO DE PRODUTOS ---")
        for p in banco_produtos:
            print(f"[{p['id']}] {p['nome']:<30} - R$ {p['preco']:.2f} (Estoque: {p['estoque']})")

        produto_selecionado = None
        while True:
            opcao_prod = input("Escolha o ID do produto: ").strip()
            for p in banco_produtos:
                if str(p["id"]) == opcao_prod:
                    produto_selecionado = p
                    break

            if produto_selecionado:
                break
            print("Opção inválida! Escolha um ID válido do catálogo.")

        # Validação da Quantidade e Estoque
        while True:
            qtd_input = input(f"Quantas unidades de '{produto_selecionado['nome']}' deseja? ")
            if qtd_input.isnumeric():
                quantidade = int(qtd_input)
                if quantidade > 0:
                    if quantidade <= produto_selecionado["estoque"]:
                        # Atualiza o estoque temporário
                        produto_selecionado["estoque"] -= quantidade
                        break
                    else:
                        print(f"Erro: Estoque insuficiente! Temos apenas {produto_selecionado['estoque']} unidades.")
                else:
                    print("Erro: Digite uma quantidade maior que zero.")
            else:
                print("Erro: Digite apenas números válidos.")

        valor_produtos = produto_selecionado["preco"] * quantidade

        # Distância e Frete
        while True:
            distancia_input = input("\nDigite a distância da entrega em km: ")
            if distancia_input.isnumeric():
                distancia = float(distancia_input)
                break
            print("Erro: Digite apenas números válidos para a distância.")

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
                print("Opção inválida! Digite 1 para Moto ou 2 para Carro.")

        valor_frete_base = distancia * tarifa_km
        taxa_rodovia = 10.00 if distancia > 20 else 0.0

        if taxa_rodovia > 0:
            print("-> Aviso: Distância superior a 20 km. Taxa de rodovia aplicada (+R$ 10.00).")

        valor_frete_total = valor_frete_base + taxa_rodovia
        valor_geral_pedido = valor_produtos + valor_frete_total

        # Emissão da Nota Fiscal
        print("\n" + "=" * 50)
        print("             NOTA FISCAL / RECIBO DE PEDIDO")
        print("=" * 50)
        print(f"Cliente:                 {cliente_logado['nome']}")
        print(f"Produto:                 {quantidade}x {produto_selecionado['nome']}")
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


    # CONSULTAR ESTOQUE

    elif opcao_menu == "2" and cliente_logado:
        print("\n--- CONSULTA DE ESTOQUE ATUALIZADO ---")
        for p in banco_produtos:
            print(f"Produto: {p['nome']:<30} | Preço: R$ {p['preco']:<6.2f} | Em Estoque: {p['estoque']} un.")


    # LOGOUT

    elif opcao_menu == "3" and cliente_logado:
        print(f"\nAté logo, {cliente_logado['nome']}! Logout realizado com sucesso.")
        cliente_logado = None

    # ----------------------------------------------------
    # SAIR
    # ----------------------------------------------------
    elif opcao_menu == "0":
        print("\nSaindo do sistema... Até logo!")
        break

    else:
        print("\nOpção inválida! Escolha uma opção do menu.")