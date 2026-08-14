def cout_letters(s):
    d = {}
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d
contagem = cout_letters("pneumoultramicroscopicossilicovulcanoconiotico")
print(contagem)