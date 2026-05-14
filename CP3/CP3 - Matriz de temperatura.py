temperaturas = [[28, 31, 34, 33], [25, 27, 29, 28], [32, 35, 36, 34], [24, 26, 25, 27]]
medias = []
critico = []


for sala in temperaturas:
    medias.append(sum(sala) / len(sala))
    count = 0

    for temp in sala:

        if temp >= 33:
            count += 1
    critico.append(count)

for i in range(len(temperaturas)):
    print(f"Sala {i+1}")
    print(f"Média: {medias[i]}")
    print(f"Registros críticos: {critico[i]} \n")

sala_critica = 0
for i in critico:
    if i > sala_critica:
        sala_critica = i

print(f"Sala com maior risco: Sala {sala_critica}")