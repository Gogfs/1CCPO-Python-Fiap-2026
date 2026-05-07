'''
▪ Escreva um algoritmo que recebe um número inteiro n > 0, cria um vetor de números reais com n
posições e preenche o vetor com n números aleatórios reais.

▪ Depois de preenchido o vetor, imprima na tela todos os números gerados.
'''
import random


n = int(input("Digite um número (maior que zero): "))
vetor = []

if n > 0:
    for i in range(n):
        vetor.append(round(random.uniform(1, 100), 4))

    print(vetor)
else:
    print("Valor inválido para n. Digite apenas números inteiros maiores que zero.")