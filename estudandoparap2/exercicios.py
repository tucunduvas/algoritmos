# Exercício 1 - Remover duplicatas mantendo a ordem
entrada1 = [3, 5, 3, 7, 9, 5, 1, 9, 2]
# Saída esperada: [3, 5, 7, 9, 1, 2]

# Exercício 2 - Girar lista para direita ou esquerda
def girar(lista, n, direcao="direita"):
    pass
# girar([1, 2, 3, 4, 5], 2, direcao="direita") → [4, 5, 1, 2, 3]

# Exercício 3 - Agrupar pares (tuplas) em um dicionário
entrada3 = [('Ana', 10), ('Bruno', 8), ('Ana', 7), ('Bruno', 9)]
# Saída esperada: {'Ana': [10, 7], 'Bruno': [8, 9]}

# Exercício 4 - Encontrar tupla com maior soma
lista4 = [(1, 2), (3, 4), (10, -1), (5, 6)]
# Saída esperada: (5, 6)

# Exercício 5 - Dicionário invertido
entrada5 = {'a': 1, 'b': 2, 'c': 1, 'd': 2}
# Saída esperada: {1: ['a', 'c'], 2: ['b', 'd']}

# Exercício 6 - Contar frequência de caracteres (ignorando espaços)
texto6 = "banana split"
# Saída esperada: {'b': 1, 'a': 3, 'n': 2, 's': 1, 'p': 1, 'l': 1, 'i': 1, 't': 1}

# Exercício 7 - Anagramas (agrupar palavras com mesmas letras)
palavras7 = ['amor', 'roma', 'carro', 'arco', 'roca']
# Saída esperada: {'amor': ['amor', 'roma'], 'carro': ['carro'], 'arco': ['arco', 'roca']}

# Exercício 8 - Matriz de adjacência
conexoes8 = [('A', 'B'), ('A', 'C'), ('B', 'C'), ('C', 'D')]
# Saída esperada:
# {
#   'A': ['B', 'C'],
#   'B': ['A', 'C'],
#   'C': ['A', 'B', 'D'],
#   'D': ['C']
# }

# Exercício 9 - Comparar duas listas de dicionários
l1_9 = [{'a': 1, 'b': 2}, {'x': 9}]
l2_9 = [{'a': 1, 'b': 2}, {'x': 9}]
l3_9 = [{'b': 2, 'a': 1}, {'x': 9}]
# True para l1_9 == l2_9 (ordem das chaves importa)

# Exercício 10 - Ordenar lista de dicionários pela chave 'idade'
dados10 = [
    {'nome': 'Ana', 'idade': 22},
    {'nome': 'Bruno', 'idade': 18},
    {'nome': 'Carlos', 'idade': 35}
]
# Saída esperada: Bruno, Ana, Carlos
