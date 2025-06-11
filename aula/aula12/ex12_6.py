
# Exercício 6: Calcular a soma dos cubos dos números que são menores que a média da lista

from functools import reduce


numeros = [1,2,3,4,5,6,7,8,9,10]

num = reduce(lambda x,y: x+y,map(lambda x: x**3, filter(lambda x: x>(reduce(lambda x,y: x+y,numeros)/ len(numeros)), numeros)))

print(num)