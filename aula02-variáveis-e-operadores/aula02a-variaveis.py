# Autor: Gabriel Oliveira - 1CCPO
import random

print("Hello, world")

'''
    bla bla bla ...
    bla bla bla ...
    bla bla bla ...
'''

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
peso = float(input("Digite seu peso: "))

print(f"Você se chama {nome}, tem {idade} anos e pesa {peso} Kg")

vetor = []

for i in range(10):
    vetor.append(random.randint(1, 100))

print("Vetor bagunçado: \n" + str(vetor))

for i in range(len(vetor)):
    for j in range(len(vetor)):
        if vetor[j] > vetor [i]:
            troca = vetor[j]
            vetor[j] = vetor[i]
            vetor[i] = troca

print("Vetor organizado: \n" + str(vetor))

for a in range(1, 15, 2):
    text = "*"*a
    print(f"'{text:^40}'")