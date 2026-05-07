'''
▪ Faça um programa que realize a soma de duas matrizes, com mesmas dimensões. Seu programa deve
ter 2 matrizes A e B de números inteiros. A terceira matriz deve ser a soma de A com B.
'''
from random import randint
import numpy as np

A = []
B = []

x = randint(2, 5)
y = randint(2, 5)

for i in range(x):
    vetor01 = []
    vetor02 = []
    for j in range(y):
        vetor01.append(randint(1, 10))
        vetor02.append(randint(1, 10))

    A.append(vetor01)
    B.append(vetor02)

A = np.array(A)
B = np.array(B)
C = A + B

print(A)
print(B)
print(C)
