
numeros = [1,2,3,4,5,6,7,8,9,10]
quadrado = list(map( lambda x: x**2, numeros))

print(quadrado)

#diferencas 
#map retorna uma transformação
#filter filtra 

pessoas = [('Ana', 19), ('João', 30), ('Maria', 20)]

crescente = list(reversed(sorted(pessoas, key = lambda x: x[1])))
print(crescente)

