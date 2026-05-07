'''
▪ Escreva um algoritmo que lê um número inteiro n, cria um vetor de inteiros de tamanho n,
faz a leitura de um conjunto de n números inteiros armazenando-os no vetor e depois calcula
a somatória dos números contidos no vetor.

▪ Dica: note que a somatória deverá ser feita após o vetor estar preenchido.
'''
from random import randint


n = int(input("Digite um número inteiro (Maior que zero): "))
vetor = []

if n > 0:
    for i in range(n):
        vetor.append(randint(1, 100))

    print(vetor)
    print(f"Somatória do vetor: {sum(vetor)}")
else:
    print("Valor inválido para n. Digite apenas números inteiros maiores que zero.")