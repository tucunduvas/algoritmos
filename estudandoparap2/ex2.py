
# Exercício 2 - Girar lista para direita ou esquerda
def girar(lista, n, direcao):
    if direcao=='direita':
        for i in range(1,n+1):
            lista[-i] = lista[0]

    print(lista)
    
girar([1, 2, 3, 4, 5], 2, direcao="direita")

def girar_direita(lista, n):
    n = n % len(lista)  # garante que n não seja maior que o tamanho da lista
    lista_rotacionada = lista[-n:] + lista[:-n]
    print(lista_rotacionada)

# Exemplo de uso
n = int(input("Digite quantas posições você quer que gire à direita: "))
girar_direita(['a', 'b', 'c', 'd'], n)
