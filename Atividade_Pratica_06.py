
import random
import string
import requests

def gerar_senha(tamanho: int) -> str:
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

def gerar_perfil_usuario():
    url = "https://randomuser.me/api/"
    resposta = requests.get(url)
    if resposta.status_code == 200:
        dados = resposta.json()
        usuario = dados['results'][0]
        nome = f"{usuario['name']['first']} {usuario['name']['last']}"
        email = usuario['email']
        pais = usuario['location']['country']
        print(f"\nNome: {nome}")
        print(f"E-mail: {email}")
        print(f"País: {pais}")
    else:
        print("Erro ao acessar a API Random User Generator.")

def consultar_cep(cep: str):
    url = f"https://viacep.com.br/ws/{cep}/json/"
    resposta = requests.get(url)
    if resposta.status_code == 200:
        dados = resposta.json()
        if "erro" in dados:
            print("CEP não encontrado.")
        else:
            print(f"\nLogradouro: {dados['logradouro']}")
            print(f"Bairro: {dados['bairro']}")
            print(f"Cidade: {dados['localidade']}")
            print(f"Estado: {dados['uf']}")
    else:
        print("Erro ao acessar a API ViaCEP.")

def consultar_cotacao(moeda: str):
    moeda = moeda.upper()
    url = f"https://economia.awesomeapi.com.br/json/last/{moeda}-BRL"
    resposta = requests.get(url)
    if resposta.status_code == 200:
        dados = resposta.json()
        chave = f"{moeda}BRL"
        if chave in dados:
            info = dados[chave]
            print(f"\nMoeda: {info['name']}")
            print(f"Valor atual: R$ {info['bid']}")
            print(f"Valor máximo: R$ {info['high']}")
            print(f"Valor mínimo: R$ {info['low']}")
            print(f"Última atualização: {info['create_date']}")
        else:
            print("Moeda não encontrada.")
    else:
        print("Erro ao acessar a API AwesomeAPI.")

def calcular_comissao():
    print("\nCalculadora de Comissão de Vendas")
    nome = input("Nome do vendedor: ")
    salario_fixo = float(input("Salário fixo (R$): "))
    vendas = float(input("Total de vendas no mês (R$): "))
    comissao = vendas * 0.15
    salario_total = salario_fixo + comissao
    print(f"\nVendedor: {nome}")
    print(f"Salário fixo: R$ {salario_fixo:.2f}")
    print(f"Comissão (15%): R$ {comissao:.2f}")
    print(f"Salário total: R$ {salario_total:.2f}")

def menu():
    while True:
        print("\n=== MENU DE ATIVIDADES ===")
        print("1 - Gerar senha aleatória")
        print("2 - Gerar perfil de usuário aleatório")
        print("3 - Consultar endereço por CEP")
        print("4 - Consultar cotação de moeda")
        print("5 - Calculadora de comissão")
        print("0 - Encerrar programa")

        opcao = input("Digite o número da opção desejada: ")

        if opcao == "1":
            try:
                tamanho = int(input("Informe o número de caracteres da senha: "))
                print("Senha gerada:", gerar_senha(tamanho))
            except ValueError:
                print("Por favor, digite um número válido.")

        elif opcao == "2":
            gerar_perfil_usuario()

        elif opcao == "3":
            cep = input("Digite o CEP (somente números): ")
            consultar_cep(cep)

        elif opcao == "4":
            moeda = input("Digite o código da moeda (ex: USD, EUR, GBP): ")
            consultar_cotacao(moeda)

        elif opcao == "5":
            calcular_comissao()

        elif opcao == "0":
            print("Encerrando o programa. Até mais!")
            break

        else:
            print("Opção inválida. Tente novamente.")

menu()
