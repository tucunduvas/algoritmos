"""
"""

# C1. Quadrados dos numeros pares
# Dada uma lista de numeros, retorne uma nova lista com os quadrados apenas dos
# numeros pares.

lista = [1,2,3,4,5,6,7,8,9]
lista_pares = [x**2 for x in lista if x%2==0]
print(lista_pares)

# C2. Filtrar strings com mais de 5 letras
# A partir de uma lista de palavras, retorne apenas as que tem mais de 5 caracteres.

lista_palavras = ['oi','para', 'gabriela', 'tucunduva']
lista_mais_cinco = [x for x in lista_palavras if len(x)>5]
print(lista_mais_cinco)

# C3. Inverter palavras
# Usando compreensao de lista, inverta cada palavra de uma lista de strings.
# Exemplo: ["casa", "gato"] → ["asac", "otag"]

lista_invertida = ['para', 'pingo']
lista_invertida_2 = [''.join(reversed(x)) for x in lista_invertida ]
print(lista_invertida_2)

# C4. Flatten de lista de listas
# A partir de uma lista de listas, crie uma lista plana.
# Exemplo: [[1,2], [3,4], [5]] → [1,2,3,4,5]

lista_listas = [[1,2],[3,4],[5]]
lista_plana = [i for x in lista_listas for i in x]
print(lista_plana)

# C5. Pares de numeros (produto cartesiano)
# Dadas duas listas de numeros, gere todos os pares possıveis entre elementos de uma
# e de outra.
# Exemplo: [1,2] e [3,4] → [(1,3), (1,4), (2,3), (2,4)]

lista1 = [1, 2]
lista2 = [3, 4]

pares = [(x, y) for x in lista1 for y in lista2]
print(pares)
