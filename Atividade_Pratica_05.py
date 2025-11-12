
import datetime
import re

# Função para calcular gorjeta
def calcular_gorjeta(valor_conta: float, porcentagem_gorjeta: float) -> float:
    return round(valor_conta * (porcentagem_gorjeta / 100), 2)

# Função para verificar se é palíndromo
def eh_palindromo(texto: str) -> str:
    texto_limpo = re.sub(r'[^a-zA-Z0-9]', '', texto).lower()
    return "Sim" if texto_limpo == texto_limpo[::-1] else "Não"

# Função para calcular preço com desconto
def calcular_desconto(preco_original: float, percentual_desconto: float) -> float:
    valor_desconto = preco_original * (percentual_desconto / 100)
    preco_final = preco_original - valor_desconto
    return round(preco_final, 2)

# Função para calcular idade em dias
def calcular_idade_em_dias(ano_nascimento: int) -> int:
    hoje = datetime.date.today()
    nascimento = datetime.date(ano_nascimento, 1, 1)
    idade_dias = (hoje - nascimento).days
    return idade_dias

# Programa principal
if __name__ == "__main__":
    print("=== Cálculo de Gorjeta ===")
    try:
        conta_input = input("Informe o valor da conta (ex: 120.50): ").replace("R$", "").strip()
        gorjeta_input = input("Informe a porcentagem da gorjeta (ex: 10): ").replace("%", "").strip()
        conta = float(conta_input)
        gorjeta = float(gorjeta_input)
        valor_gorjeta = calcular_gorjeta(conta, gorjeta)
        print(f"Gorjeta: R$ {valor_gorjeta:.2f}")
    except ValueError:
        print("Erro: Digite apenas números válidos para o valor da conta e a porcentagem.")

    print("\n=== Verificação de Palíndromo ===")
    texto = input("Digite uma palavra ou frase: ")
    print(f"É palíndromo? {eh_palindromo(texto)}")

    print("\n=== Cálculo de Desconto ===")
    try:
        preco_input = input("Informe o preço original do produto (ex: 250.75): ").replace("R$", "").strip()
        percentual_input = input("Informe o percentual de desconto (ex: 10): ").replace("%", "").strip()
        preco = float(preco_input)
        percentual = float(percentual_input)
        preco_final = calcular_desconto(preco, percentual)
        print(f"Preço com desconto: R$ {preco_final:.2f}")
    except ValueError:
        print("Erro: Certifique-se de digitar apenas números válidos para o preço e o desconto.")

    print("\n=== Cálculo de Idade em Dias ===")
    try:
        ano = int(input("Informe o ano de nascimento (ex: 1990): "))
        idade_dias = calcular_idade_em_dias(ano)
        print(f"Você tem aproximadamente {idade_dias} dias de vida.")
    except ValueError:
        print("Erro: Digite um ano válido.")