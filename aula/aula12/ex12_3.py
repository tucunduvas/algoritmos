# Exercício 3: Somar os quadrados dos números que são múltiplos de 3

from functools import reduce


num = [1,2,3,4,5,6,7,8,9,10]

soma = reduce(lambda x,y: x+y ,map(lambda x: x**2 ,filter(lambda x: x%3==0, num)))
print(soma)