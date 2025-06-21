nomes = (('gabi', 18), ('maria', 19), ('alice', 35),('edi', 40), ('pingo', 75) )

maior_30 = tuple([x for x,j in nomes if j>30])
print(maior_30)

maior = list(filter( lambda item: item[1]>30, nomes))
print(maior)

map_filter = list(map(lambda item: item[0], filter(lambda item: item[1]>30, nomes)))

print(map_filter)