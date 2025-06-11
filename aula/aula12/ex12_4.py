
# Exercício 4: Calcular o produto dos números pares após multiplicar por 2 

from functools import reduce

numeros = [1,2,3,4,5,6,7,8,9,10]

produto = reduce(lambda x,y: x*y, map(lambda x: x**2 ,filter(lambda x: x%2==0, numeros)))

print(produto)
