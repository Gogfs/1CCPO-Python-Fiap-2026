print("Exercício 1")

raio = 5
pi = 3.14
area = pi * raio ** 2

print(f"A área de uma circuferência com raio = {raio} é {area}")

print("="*40)
print("Exercício 2")

f = float(input("Digite uma temperatura em graus Fahrenheit: "))
c = (f - 32) * 5 / 9
print(f"{f} graus Fahrenheit equivale a {c} graus Celsius")

print("="*40)
print("Exercício 3")

livros = 3 * 25
canetas = 2 * 5
print(f"O valor total gasto com o material foi R${livros + canetas}")

print("="*40)
print("Exercício 4")

velocidade = 60
distancia = 150
tempo = distancia / velocidade
print(f"O tempo que o carro levou para percorrer a distância foi {tempo}")

print("="*40)
print("Exercício 5")

a = float(input("Digite a primeira nota: "))
b = float(input("Digite a segunda nota: "))
print(f"A média do aluno foi {(a + b) / 2}")

print("="*40)
print("Exercício 6")

a = 4 * float(input("Digite a primeira nota: "))
b = 6 * float(input("Digite a segunda nota: "))
print(f"A média do aluno foi {(a + b) / 2}")

print("="*40)
print("Exercício 7")

peca1 = input("Digite o nome da peça 1: ")
qtde_peca1 = int(input(f"Informe quantas {peca1} você deseja: "))
preco_peca1 = float(input(f"Informe o preço da unidade de {peca1}. Seja honesto: "))

peca2 = input("Digite o nome da peça 2: ")
qtde_peca2 = int(input(f"Informe quantas {peca2} você deseja: "))
preco_peca2 = float(input(f"Informe o preço da unidade de {peca2}. Seja honesto: "))

preco = qtde_peca1 * preco_peca1 + qtde_peca2 * preco_peca2
print(f"O valor de {qtde_peca1} {peca1}(s) é {qtde_peca1 * preco_peca1} \n O valor de {qtde_peca2} {peca2}(s) é {qtde_peca2 * preco_peca2} \n O preço total da compra é {preco}")

print("="*40)
print("Exercício 8")

produto = float(input("Informe o valor do produto: "))
valor_pago = float(input("Informe o valor pago: "))
troco = valor_pago - produto
print(f"Seu troco é {troco}")
