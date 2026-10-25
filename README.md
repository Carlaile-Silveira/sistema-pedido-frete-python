# Sistema de Pedido, Frete e Nota Fiscal (Python - Mundo 1)

Projeto desenvolvido como parte dos estudos práticos de lógica de programação em Python, aplicando os conceitos fundamentais do **Mundo 1** para resolver uma dor real de negócio: o cálculo automatizado de pedidos, a gestão de um catálogo de produtos e a precificação de taxas de frete para entregas comerciais.

## 🚀 Funcionalidades do Sistema
- **Identificação com Validação:** Validação rigorosa do nome do cliente (garantindo apenas letras e formatação automática das iniciais com `.title()`).
- **Catálogo de Produtos Integrado:** Seleção interativa de itens pré-cadastrados (como caixas de brigadeiros e tortas) com cálculo automático do subtotal por quantidade.
- **Cálculo Dinâmico de Frete:** Definição da tarifa por quilómetro com base no tipo de veículo escolhido (**Moto** ou **Carro**).
- **Regras de Negócio Avançadas:** Aplicação automática de uma taxa extra de rodovia para entregas superiores a 20 km.
- **Emissão de Recibo / Nota Fiscal:** Exibição estruturada e formatada (utilizando `f-strings` e precisão decimal `:.2f`) de todo o resumo financeiro do pedido.

## 🛠️ Conceitos Técnicos Aplicados
- Variáveis e Tipos de Dados (`str`, `int`, `float`)
- Entrada e Saída de Dados (`input`, `print`)
- Manipulação avançada de Strings (`.strip()`, `.title()`, `.replace()`, `.isalpha()`)
- Estruturas Condicionais (`if`, `elif`, `else`)
- Controlo de Fluxo para Validações (`while True` com `break`)

## 💻 Como Executar o Projeto
1. Certifique-se de ter o **Python 3.12+** instalado no seu computador.
2. Clone este repositório ou faça o download dos ficheiros.
3. Abra o projeto no **PyCharm** e execute o script no terminal:
   ```bash
   python main.py