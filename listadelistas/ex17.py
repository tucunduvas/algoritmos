"""
15. Dada a lista ["A", "B", "C"], use pop para remover e imprimir o ´ultimo elemento.
16. Crie uma lista de 5 elementos e substitua o segundo elemento pelo valor 99.
1
17. Crie uma lista com 5 n´umeros e calcule a m´edia usando la¸co for.

"""

lista = [5,6,8,9,4]

soma = 0
for elemento in lista: 
    soma += elemento
    media = soma/len(lista)
    
print(f"a média é: {media}")

#outro jeito de fazer

var =sum(lista)/len(lista)
print(var)