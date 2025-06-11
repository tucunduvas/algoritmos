# Exercício 5: Encontrar a média dos números que são maiores que 5 após elevar ao quadrado 

from functools import reduce


numeros = [1,2,3,4,5,6,7,8,9,10]

media = reduce(lambda x,y: x+y, map(lambda x: x**2, filter(lambda x: x>5, numeros)))/list( filter(lambda x: x>5, numeros))
print(media)


