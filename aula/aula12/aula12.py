
from functools import reduce
from random import randint

"""
map 
transformar um iterável

filtrer
aplica uma condição, devolve um novo array dos itens que passaram na condição

reduce 
aplica uma função de dois argumentos cumulativamente aos itens de um iterável
reduz a um unico valor
pega uma lista, da esquerda para direita ele aplica alguma coisa e reduz

sintaxe

from functools import reduce
reduce(func, array)

a funcao recebe dois argumentos

reduce(func, array, tem como colocar de qual começa)
"""

numeros = [1,2,3,4,5,6,7]

soma_total = reduce(lambda x,y: x+y, numeros)
print(soma_total)

numeros_random = [randint(1,50) for _ in range(10)]

max_numero = reduce( lambda x,y: x if x>y else y, numeros)

# Exercicio 1: Calcular a media dos quadrados do números pares de uma lista 

nums = [1,2,3,4,5,6,7,8,9,10]

media = reduce( lambda x,y: x+y, map(lambda x: x**2, filter(lambda x: x%2==0,nums)))/ len(list(filter(lambda x: x%2==0,nums)))
print(f"media {media}")


# Exercício 2: Encontrar o maior número ímpar após elevar ao cubo
# Exercício 3: Somar os quadrados dos números que são múltiplos de 3
# Exercício 4: Calcular o produto dos números pares após multiplicar por 2 
# Exercício 5: Encontrar a média dos números que são maiores que 5 após elevar ao quadrado 
# Exercício 6: Calcular a soma dos cubos dos números que são menores que a média da lista










numeros = [1,2,3,4,5,6,7,8,9,10]
quadrado = list(map( lambda x: x**2, numeros))

print(quadrado)

#diferencas 
#map retorna uma transformação
#filter filtra 

pessoas = [('Ana', 19), ('João', 30), ('Maria', 20)]

crescente = list(reversed(sorted(pessoas, key = lambda x: x[1])))
print(crescente)

maiores_60 = list(filter(lambda x: x>60, numeros))

print("Ex 1 - números maiores que 60: ", maiores_60)

maiores_media = list(filter(lambda x: x>(sum(numeros)/len(numeros)), numeros))





