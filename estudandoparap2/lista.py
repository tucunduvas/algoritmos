# Criação de lista
lista = [1, 2, 3, 4, 5]

# Acessar elementos
print(lista[0])  # 1
print(lista[-1])  # 5 (último elemento)

# Fatiamento
print(lista[1:4])  # [2, 3, 4]

# Adicionar elemento no final
lista.append(6)

# Inserir elemento em uma posição específica
lista.insert(2, 99)  # insere 99 na posição 2

# Concatenar listas
lista2 = [7, 8]
lista3 = lista + lista2

# Estender lista com outra lista
lista.extend([9, 10])

# Remover elemento por valor
lista.remove(99)

# Remover elemento por índice
removido = lista.pop(2)  # remove elemento no índice 2 e retorna

# Limpar a lista
lista.clear()

# Copiar lista
lista = [1, 2, 3]
copia = lista.copy()

# Contar quantas vezes um elemento aparece
print(lista.count(2))  # 1

# Obter índice de um elemento
print(lista.index(3))  # 2

# Inverter a ordem dos elementos
lista.reverse()

# Ordenar lista (em ordem crescente)
lista.sort()

# Ordenar lista em ordem decrescente
lista.sort(reverse=True)

# Verificar se um valor está na lista
print(2 in lista)  # True

# Iterar sobre lista
for item in lista:
    print(item)

# List comprehension (compreensão de lista)
quadrados = [x**2 for x in range(5)]  # [0, 1, 4, 9, 16]

# Filtrar elementos com list comprehension
pares = [x for x in range(10) if x % 2 == 0]  # [0, 2, 4, 6, 8]
