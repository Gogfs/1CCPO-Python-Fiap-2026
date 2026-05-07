# Atividade 2 - Matriz

matriz = []

numero = 1
for i in range(4):
    vetor = []
    for j in range(5):
        vetor.append(numero)
        numero += 1
    matriz.append(vetor)

print(matriz)