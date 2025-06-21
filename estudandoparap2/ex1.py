# Exercício 1 - Remover duplicatas mantendo a ordem
entrada1 = [3, 5, 3, 7, 9, 5, 1, 9, 2]
# Saída esperada: [3, 5, 7, 9, 1, 2]

# for i in entrada1:
#     if entrada1.count(i)>1:
#         index = entrada1.index(i)
#         entrada1.pop()
        
# print("_____________")
# for j in reversed(entrada1):
#     if entrada1.count(j)>1:
#         entrada1.remove(j)
    
# print("e", entrada1)

lista = []

for i in entrada1:
    if i not in lista:
        lista.append(i)

print(lista)


""" 
for i in entrada1:
    for i in range(len(entrada1),0):
    
        if entrada1.count(i)>1:
            entrada1.remove(i)
            

"""

""" 
funcoes de excluir

"""

# Lista original
lista1 = [1, 2, 3, 2]
lista1.remove(2)  # remove a primeira ocorrência do valor 2
print("remove():", lista1)  # [1, 3, 2]

# pop(): remove pelo índice (ou o último se nenhum índice for passado)
lista2 = ['a', 'b', 'c']
lista2.pop()  # remove 'c'
lista2.pop(0)  # remove 'a'
print("pop():", lista2)  # ['b']

# del: remove pelo índice
lista3 = [10, 20, 30, 40]
del lista3[1]  # remove 20
print("del:", lista3)  # [10, 30, 40]

# List comprehension: remove todas as ocorrências de 2
lista4 = [1, 2, 3, 4, 2]
lista4 = [x for x in lista4 if x != 2]
print("list comprehension:", lista4)  # [1, 3, 4]

# clear(): remove todos os elementos da lista
lista5 = [1, 2, 3]
lista5.clear()
print("clear():", lista5)  # []
