lista = [1,2,3,4,5,6,7,8,6,8,9,10,10]
6+8+10

lista2 = []
for i in lista:
    if lista.count(i)>1:
        if i not in lista2:
            lista2.append(i)
        
print(sum(lista2))
lista3 = [x for x in lista if lista.count(x)>1]
lista3 = set(lista3)
print(sum(lista3))


print(set(filter(lambda x: x if lista.count(x)>1 else "", lista)))