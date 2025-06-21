lista = 1,2,3,4,2,5,6,9,6,7,8,7

lista2 = list()

for i in lista:
    if i not in lista2:
        lista2.append(i)
        
print(lista2)