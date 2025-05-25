"""
6. Solicite 5 n´umeros ao usu´ario e armazene em uma lista. Em seguida, imprima o
maior e o menor n´umero

"""
lista = list()
for i in range(5):
    num = int(input("degite 5 número: "))
    lista.append(num)

n = max(lista)
k = min(lista)

print(f"O menor número é: {k}")
print(f"O maior número é: {n}")

#outro jeito 
lista.sort()
menor = lista[0]
maior = lista[-1]
print(f"O menor número é: {menor}")
print(f"O maior número é: {maior}")