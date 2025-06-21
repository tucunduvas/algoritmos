num1 = int(input("Digite um número: "))
num2 = int(input("Digite um número: "))
num3 = int(input("Digite um número: "))

tupla = []
tupla.append(num1)
tupla.append(num2)
tupla.append(num3)
tupla = tuple(tupla)

for i, valor in enumerate(tupla):
    if valor==2:
        print(f"O número 2 está na posição {i}")
count5 = tupla.count(5)

pares  = tuple((x for x in tupla if x%2==0))

print(f"O número 5 aperece {count5} vezes")
print(f"Números pares: {pares}")


