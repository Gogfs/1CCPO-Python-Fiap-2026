# noinspection LanguageDetectionInspection
'''
▪ Faça um programa que tenha 2 vetores. Um vetor para os meses e outros para a quantidade de dias
para cada mês.

▪ Seu programa deve exibir mensagens da seguinte forma:
▪ O Mês de Jan tem 31 dias ao t-odo.
▪ O mês de Fev tem 28 dias ao t-odo.
▪ O mês de Mar tem 31 dias ao t-odo.
▪ ...
▪ O mês de Dez tem 31 dias ao t-odo.
'''

meses = ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun", "Jul", "Ago", "Set", "Out", "Nov", "Dez"]
dias_meses = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

for i in range(12):
    print(f"O Mês de {meses[i]} tem {dias_meses[i]} dias ao todo")