
# Atividade Prática 03

# 1 - Área da circunferência
print("1 - Área da Circunferência")
raio = float(input("Digite o valor do raio: "))
pi = 3.14159265
area = pi * raio ** 2
print(f"A={area:.4f}\n")

# 2 - Classificador de Idade
print("2 - Classificador de Idade")
idade = int(input("Digite sua idade: "))
if idade <= 12:
    categoria = "Criança"
elif idade <= 17:
    categoria = "Adolescente"
elif idade <= 59:
    categoria = "Adulto"
else:
    categoria = "Idoso"
print(f"Classificação: {categoria}\n")

# 3 - Calculadora de IMC
print("3 - Calculadora de IMC")
peso = float(input("Digite seu peso (kg): "))
altura = float(input("Digite sua altura (m): "))
imc = peso / (altura ** 2)
if imc < 18.5:
    classificacao = "Abaixo do peso"
elif imc < 25:
    classificacao = "Peso normal"
elif imc < 30:
    classificacao = "Sobrepeso"
else:
    classificacao = "Obeso"
print(f"IMC: {imc:.2f}")
print(f"Classificação: {classificacao}\n")

# 4 - Conversor de Temperatura
print("4 - Conversor de Temperatura")
temp = float(input("Digite a temperatura: "))
origem = input("Unidade de origem (C/F/K): ").upper()
destino = input("Converter para (C/F/K): ").upper()

resultado = None
if origem == "C":
    if destino == "F":
        resultado = (temp * 9/5) + 32
    elif destino == "K":
        resultado = temp + 273.15
    else:
        resultado = temp
elif origem == "F":
    if destino == "C":
        resultado = (temp - 32) * 5/9
    elif destino == "K":
        resultado = (temp - 32) * 5/9 + 273.15
    else:
        resultado = temp
elif origem == "K":
    if destino == "C":
        resultado = temp - 273.15
    elif destino == "F":
        resultado = (temp - 273.15) * 9/5 + 32
    else:
        resultado = temp

print(f"Temperatura convertida: {resultado:.2f} {destino}\n")

# 5 - Verificador de Ano Bissexto
print("5 - Verificador de Ano Bissexto")
ano = int(input("Digite o ano: "))
bissexto = (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)
print("Ano bissexto." if bissexto else "Ano não bissexto.\n")

# 6 - Calculadora de Comissão
print("6 - Calculadora de Comissão")
nome = input("Nome do vendedor: ")
salario_fixo = float(input("Salário fixo: R$ "))
vendas = float(input("Total de vendas no mês: R$ "))
comissao = vendas * 0.15
total = salario_fixo + comissao
print(f"TOTAL = R$ {total:.2f}\n")

# 7 - Calculadora da Média
print("7 - Calculadora da Média")
N1 = float(input("Nota 1: "))
N2 = float(input("Nota 2: "))
N3 = float(input("Nota 3: "))
N4 = float(input("Nota 4: "))

media = (N1 * 2 + N2 * 3 + N3 * 4 + N4 * 1) / 10
print(f"Media: {media:.1f}")

if media >= 7.0:
    print("Aluno aprovado.")
elif media < 5.0:
    print("Aluno reprovado.")
else:
    print("Aluno em exame.")
    nota_exame = float(input("Nota do exame: "))
    print(f"Nota do exame: {nota_exame:.1f}")
    media_final = (media + nota_exame) / 2
    if media_final >= 5.0:
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")
    print(f"Media final: {media_final:.1f}")