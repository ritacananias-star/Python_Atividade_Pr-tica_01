
# Atividade Prática - Parte 4

# 1 - Calculadora com tratamento de erros
print("1 - Calculadora com tratamento de erros")
while True:
    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        operacao = input("Digite a operação (+, -, *, /): ")

        if operacao == "+":
            resultado = num1 + num2
        elif operacao == "-":
            resultado = num1 - num2
        elif operacao == "*":
            resultado = num1 * num2
        elif operacao == "/":
            if num2 == 0:
                raise ZeroDivisionError("Divisão por zero não permitida.")
            resultado = num1 / num2
        else:
            raise ValueError("Operação inválida.")

        print(f"Resultado: {resultado}")
        break

    except ValueError as ve:
        print(f"Erro: {ve}. Tente novamente.\n")
    except ZeroDivisionError as zde:
        print(f"Erro: {zde}. Tente novamente.\n")

# 2 - Registro de notas da turma
print("\n2 - Registro de notas da turma")
notas = []
while True:
    entrada = input("Digite uma nota (ou 'fim' para encerrar): ")
    if entrada.lower() == "fim":
        break
    try:
        nota = float(entrada)
        if 0 <= nota <= 10:
            notas.append(nota)
        else:
            print("Nota inválida. Digite um valor entre 0 e 10.")
    except ValueError:
        print("Entrada inválida. Digite um número ou 'fim'.")

if notas:
    media = sum(notas) / len(notas)
    print(f"Média da turma: {media:.2f}")
else:
    print("Nenhuma nota válida foi registrada.")

# 3 - Verificador de senha forte
print("\n3 - Verificador de senha forte")
import re
while True:
    senha = input("Digite uma senha (ou 'sair' para encerrar): ")
    if senha.lower() == "sair":
        print("Encerrando verificação de senha.")
        break
    if len(senha) >= 8 and re.search(r"\d", senha):
        print("Senha forte!")
        break
    else:
        print("Senha fraca. Deve ter pelo menos 8 caracteres e conter um número.")

# 4 - Verificador de par ou ímpar
print("\n4 - Verificador de par ou ímpar")
pares = 0
impares = 0

while True:
    entrada = input("Digite um número inteiro (ou 'fim' para encerrar): ")
    if entrada.lower() == "fim":
        break
    try:
        numero = int(entrada)
        if numero % 2 == 0:
            print("Número par.")
            pares += 1
        else:
            print("Número ímpar.")
            impares += 1
    except ValueError:
        print("Entrada inválida. Digite um número inteiro.")

print(f"Quantidade de números pares: {pares}")
print(f"Quantidade de números ímpares: {impares}")