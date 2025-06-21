# Exercício 4 - Encontrar tupla com maior soma
lista4 = [(1, 2), (3, 4), (10, -1), (5, 6)]
# Saída esperada: (5, 6)
        
lista = [max(x) for x in lista4 ]
print(lista)

print(max(lista4, key=sum))


# Lista de tuplas - maior soma
lista1 = [(1, 2), (3, 4), (10, -1), (5, 6)]
maior_soma = max(lista1, key=sum)
print("Tupla com maior soma:", maior_soma)

# Lista de strings - maior comprimento
nomes = ["ana", "maria", "joão", "alexandra"]
mais_longo = max(nomes, key=len)
print("Nome mais longo:", mais_longo)

# Lista de palavras - menor ordem alfabética ignorando maiúsculas
palavras = ["Banana", "abacaxi", "Caju"]
ordem_alfabetica = min(palavras, key=str.lower)
print("Menor (ordem alfabética, ignorando maiúsculas):", ordem_alfabetica)

# Lista de números - menor valor absoluto
numeros = [-10, 5, -7]
menor_abs = min(numeros, key=abs)
print("Número com menor valor absoluto:", menor_abs)

# Função definida pelo usuário - diferença entre elementos da tupla
def diferenca_tupla(t):
    return abs(t[0] - t[1])

lista2 = [(1, 10), (5, 3), (4, 4)]
maior_diferenca = max(lista2, key=diferenca_tupla)
print("Tupla com maior diferença entre elementos:", maior_diferenca)

# Lambda para comparar primeiro e segundo valor da tupla
lista3 = [(1, 2), (3, 4), (5, 6)]
maior_primeiro = max(lista3, key=lambda x: x[0])
maior_segundo = max(lista3, key=lambda x: x[1])
print("Tupla com maior primeiro valor:", maior_primeiro)
print("Tupla com maior segundo valor:", maior_segundo)
