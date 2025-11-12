
import csv
import json
import pandas as pd

# 1️⃣ Ler log de treinamento e calcular média e desvio padrão
def analisar_log_treinamento(caminho_arquivo):
    try:
        df = pd.read_csv(caminho_arquivo)
        media = df['tempo_execucao'].mean()
        desvio_padrao = df['tempo_execucao'].std()
        print(f"\n📈 Análise do Log de Treinamento:")
        print(f"Média do tempo de execução: {media:.2f}")
        print(f"Desvio padrão: {desvio_padrao:.2f}")
    except Exception as e:
        print(f"Erro ao analisar o log: {e}")

# 2️⃣ Escrever dados pessoais em um arquivo CSV
def escrever_csv_pessoas(caminho_arquivo):
    dados = [
        {'Nome': 'Ana', 'Idade': 28, 'Cidade': 'Recife'},
        {'Nome': 'Carlos', 'Idade': 35, 'Cidade': 'Olinda'},
        {'Nome': 'Beatriz', 'Idade': 22, 'Cidade': 'Jaboatão'}
    ]
    try:
        with open(caminho_arquivo, mode='w', newline='', encoding='utf-8') as arquivo:
            campos = ['Nome', 'Idade', 'Cidade']
            escritor = csv.DictWriter(arquivo, fieldnames=campos)
            escritor.writeheader()
            escritor.writerows(dados)
        print(f"\n✅ Arquivo CSV '{caminho_arquivo}' criado com sucesso.")
    except Exception as e:
        print(f"Erro ao escrever CSV: {e}")

# 3️⃣ Ler e exibir dados de um arquivo CSV
def ler_csv_pessoas(caminho_arquivo):
    try:
        print(f"\n📋 Dados do arquivo CSV '{caminho_arquivo}':")
        with open(caminho_arquivo, mode='r', encoding='utf-8') as arquivo:
            leitor = csv.DictReader(arquivo)
            for linha in leitor:
                print(f"Nome: {linha['Nome']}, Idade: {linha['Idade']}, Cidade: {linha['Cidade']}")
    except Exception as e:
        print(f"Erro ao ler CSV: {e}")

# 4️⃣ Ler e escrever dados em um arquivo JSON
def manipular_json_pessoa(caminho_arquivo):
    pessoa = {
        'nome': 'João',
        'idade': 30,
        'cidade': 'Petrolina'
    }
    try:
        with open(caminho_arquivo, 'w', encoding='utf-8') as arquivo:
            json.dump(pessoa, arquivo, ensure_ascii=False, indent=4)
        print(f"\n✅ Arquivo JSON '{caminho_arquivo}' criado com sucesso.")

        with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
            dados = json.load(arquivo)
            print(f"\n📄 Dados do JSON:")
            print(f"Nome: {dados['nome']}, Idade: {dados['idade']}, Cidade: {dados['cidade']}")
    except Exception as e:
        print(f"Erro ao manipular JSON: {e}")

# 🔁 Execução dos scripts
if __name__ == "__main__":
    analisar_log_treinamento('log_treinamento.csv')
    escrever_csv_pessoas('pessoas.csv')
    ler_csv_pessoas('pessoas.csv')
    manipular_json_pessoa('pessoa.json')