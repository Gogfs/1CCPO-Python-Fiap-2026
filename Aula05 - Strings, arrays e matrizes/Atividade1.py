# Atividade 1: Duplas

nomes = []

for i in range(4):
    nomes.append(input("Digite um nome: "))

count = 1
for i in range(len(nomes)):
    for j in range(len(nomes)):
        if i == j:
            continue
        print(f"{count}º Dupla: {nomes[i]} e {nomes[j]}")
        count += 1