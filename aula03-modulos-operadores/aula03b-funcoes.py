from random import randint

def criar_vetor(n_posicoes, limite):
    vetor = []
    for i in range(n_posicoes):
        vetor.append(randint(1, limite))

    return vetor

def organizar_vetor(vetor):
    for i in range(len(vetor)):
        for j in range(len(vetor)):
            if vetor[j] > vetor[i]:
                vetor[i], vetor[j] = vetor[j], vetor[i]
    return vetor

array = criar_vetor(10, 100)
print(str(array))
print(str(organizar_vetor(array)))