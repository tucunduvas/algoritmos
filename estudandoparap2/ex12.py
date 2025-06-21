# def transposta(lista):
#     for i in lista:
#         for j in i: 
#             return print(j, end= "")
#     print(" ")
# transposta([[1,2,3],[4,5,6]])
lista = [[1,2,3],[4,5,6]]
for i in lista:
    for j in i: 
        print(j,end= " ")
        print(" ")    

for i, x in enumerate(lista):
    print([lista[x][i], lista[j][i]])
    