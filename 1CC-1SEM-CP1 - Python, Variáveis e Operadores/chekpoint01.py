print("Iniciando programa...")

produto = input("Informe o nome do produto: ")
preco_unitario = float(input("Informe o preço unitário do produto: "))
quantidade_comprada = int(input("Informe a quantidade comprada: "))
desconto_percentual = int(input("Informe o a porcentagem do desconto (0 a 100): ")) / 100

print("\n")

valor_bruto = preco_unitario * quantidade_comprada
desconto = valor_bruto * desconto_percentual

print(f"Produto: {produto}")
print(f"Valor bruto: R$ {valor_bruto:.2f}")
print(f"Desconto: R$ {desconto:.2f}")
print(f"Valor final: R$ {valor_bruto - desconto:.2f}")



print("Iniciando programa...")

nome = input("Informe o nome do programador: ")
valor_hora = float(input("Informe o valor da hora trabalhada: "))
hora_trabalhada_mes = int(input("Informe a quantidade horas trabalhadas no mês: "))
bonus = float(input("Informe o valor do bônus: "))
desconto_percentual = int(input("Informe o valor percentual do desconto (0 a 100): ")) / 100

print("\n")

salario_bruto = valor_hora * hora_trabalhada_mes + bonus
desconto = salario_bruto * desconto_percentual

print(f"Colaborador: {nome}")
print(f"Horas trabalhadas no mês: {hora_trabalhada_mes} horas")
print(f"Bônus: {bonus:.2f}")
print(f"Salário bruto: R$ {salario_bruto:.2f}")
print(f"Desconto: R$ {desconto:.2f}")
print(f"Valor final: R$ {salario_bruto - desconto:.2f}")
