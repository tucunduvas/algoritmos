"""
R5. Busca bin´aria recursiva
Implemente a busca bin´aria de forma recursiva para uma lista ordenada.

"""

def buscabinaria(lista, valor_procurado):
    if valor_procurado:
        return lista.index(valor_procurado)
    if lista[len(lista)]//2 == valor_procurado:
        return lista.index[valor_procurado]
    elif lista[len(lista)//2] == valor_procurado:
        return lista.index[valor_procurado]
    elif lista[len(lista)//2]>valor_procurado:
        return buscabinaria([x for x in lista if x>lista[len(lista)//2]], valor_procurado)
    elif lista[len(lista)//2]<valor_procurado:
        return buscabinaria([x for x in lista if x<lista[len(lista//2)]], valor_procurado)
        
    
print(buscabinaria([2, 5, 8, 12, 16, 23, 38, 56, 72, 91], 23))

def buscabinaria(lista, valor_procurado):
    if not lista:
        return None 

    meio = len(lista) // 2

    if lista[meio] == valor_procurado:
        return lista[meio]
    elif valor_procurado < lista[meio]:
        return buscabinaria([x for x in lista[:meio]], valor_procurado)
    else:
        return buscabinaria([x for x in lista[meio+1:]], valor_procurado)

# Exemplo
print(buscabinaria([2, 5, 8, 12, 16, 23, 38, 56, 72, 91], 23))  # Saída: 23


def buscabinaria(lista, valor_procurado, inicio=0, fim=None):
    if fim is None:
        fim = len(lista) - 1

    if inicio > fim:
        return -1  # Não encontrado

    meio = (inicio + fim) // 2

    if lista[meio] == valor_procurado:
        return meio
    elif lista[meio] > valor_procurado:
        return buscabinaria(lista, valor_procurado, inicio, meio - 1)
    else:
        return buscabinaria(lista, valor_procurado, meio + 1, fim)

# Exemplo de uso
print(buscabinaria([2, 5, 8, 12, 16, 23, 38, 56, 72, 91], 23))  # Saída: 5


# lista = [10, 20, 30, 40,50,60,70]
# lista_maior = [x for x in lista if x>lista[len(lista)//2]]
# meio = len(lista) // 2
# print("Segundo elemento central:", lista[meio])

# print(lista_maior)