'''
▪ Escreva um algoritmo que recebe uma lista de nomes e imprime os nomes na ordem inversa a da
leitura.

▪ A lista termina quando o usuário aperta o Enter sem que nenhum nome tenha sido digitado.
'''

nomes = []

while True:
    nomes.append(input("Digite um nome: "))
    if nomes[-1] == '':
        nomes.pop()
        break

print(nomes[::-1])