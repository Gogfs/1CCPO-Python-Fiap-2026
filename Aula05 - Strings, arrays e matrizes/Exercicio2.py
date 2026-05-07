'''
▪ Considere uma turma de n alunos onde desejamos calcular a média das notas da prova semestral e
saber quantas notas estão iguais, acima e abaixo dessa média.

▪ Escreva um algoritmo que lê um inteiro n representando a quantidade de alunos e cada uma das n
notas e mostra a média da turma, quantas notas são iguais, acima e abaixo da média da turma.
'''

num_alunos = int(input("Informe quantos alunios tem na sala: "))
notas = []

for i in range(num_alunos):
    notas.append(int(input(f"Digite a nota da prova semestral do {i + 1}º aluno: ")))

media = sum(notas) / len(notas)
print(f"\nMédia da turma: {media}")
print(f"Número de alunos abaixo da média: {sum(1 for x in notas if x < media)}")
print(f"Número de alunos na média: {sum(1 for x in notas if x == media)}")
print(f"Número de alunos acima da média: {sum(1 for x in notas if x > media)}")
