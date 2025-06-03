import random
from random import randint
from random import randrange

"""
Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.

Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.

"""
for i in range(5):
    tupla = random.randint(1,5)
    
print(tupla)

# print(sorted(tupla))
# print(a[0])
# print(a[-1])