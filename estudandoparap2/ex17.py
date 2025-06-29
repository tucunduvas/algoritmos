from functools import reduce


produtos = [('shampoo', 60), ('pasta', 10), ('bacalhau', 100), ('creme', 20)]
soma = 0

media = sum(p[1] for p in produtos)/ len(produtos)
media2 = [x for x,j in produtos if j>media ]

filtro = list(filter(lambda item: item[1]>media, produtos))
print(media)
print(media2)
print(filtro)