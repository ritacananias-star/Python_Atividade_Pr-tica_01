
# Atividade Prática 02

# 1 - Conversor de Moeda
valor_reais = 100.00
taxa_dolar = 5.60
taxa_euro = 6.60

valor_dolar = round(valor_reais / taxa_dolar, 2)
valor_euro = round(valor_reais / taxa_euro, 2)

print("1 - Conversor de Moeda")
print(f"Valor em reais: R$ {valor_reais:.2f}")
print(f"Convertido em dólares: US$ {valor_dolar:.2f}")
print(f"Convertido em euros: € {valor_euro:.2f}\n")

# 2 - Calculadora de Desconto
nome_produto = "Camiseta"
preco_original = 50.00
porcentagem_desconto = 20

valor_desconto = round(preco_original * (porcentagem_desconto / 100), 2)
preco_final = round(preco_original - valor_desconto, 2)

print("2 - Calculadora de Desconto")
print(f"Produto: {nome_produto}")
print(f"Preço original: R$ {preco_original:.2f}")
print(f"Desconto: {porcentagem_desconto}%")
print(f"Valor do desconto: R$ {valor_desconto:.2f}")
print(f"Preço final: R$ {preco_final:.2f}\n")

# 3 - Calculadora de Média Escolar
nota1 = 7.5
nota2 = 8.0
nota3 = 6.5

media = round((nota1 + nota2 + nota3) / 3, 2)

print("3 - Calculadora de Média Escolar")
print(f"Nota 1: {nota1}")
print(f"Nota 2: {nota2}")
print(f"Nota 3: {nota3}")
print(f"Média final: {media:.2f}\n")

# 4 - Calculadora de Consumo de Combustível
distancia = 300  # km
combustivel = 25  # litros

consumo_medio = round(distancia / combustivel, 2)

print("4 - Calculadora de Consumo de Combustível")
print(f"Distância percorrida: {distancia} km")
print(f"Combustível gasto: {combustivel} litros")
print(f"Consumo médio: {consumo_medio:.2f} km/l\n")

# 5 - Calculadora de Soma com Entrada do Usuário
print("5 - Calculadora de Soma com Entrada do Usuário")
A = int(input("Digite o valor de A: "))
B = int(input("Digite o valor de B: "))
X = A + B
print(f"X = {X}\n")

# 6 - Calculadora de salário por horas trabalhadas
print("6 - Calculadora de salário por horas trabalhadas")
numero_funcionario = int(input("Número do funcionário: "))
horas_trabalhadas = int(input("Horas trabalhadas: "))
valor_por_hora = float(input("Valor por hora: "))
salario = round(horas_trabalhadas * valor_por_hora, 2)
print(f"Número do funcionário = {numero_funcionario}")
print(f"Salário = R$ {salario:.2f}")