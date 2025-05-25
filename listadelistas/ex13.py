"""
    13. Crie uma lista com os n´umeros de 1 a 10 usando range() e imprima somente os
pares.
"""

lista = list()

for i in range(1,11):
    lista.append(i)

for elemento in lista:
    if elemento%2==0:
        print(elemento)