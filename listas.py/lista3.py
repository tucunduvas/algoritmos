n = int(input("Quantos números você vai digitar? "))

vet: list[float] = [0 for x in range(n)]

for i in range(0,n):
    vet[i] = float(input("digite um número: "))
    
print(" ")
print("NÚMEROS DIGITADOS: ")

for i in range(0,n):
    print(f"{vet[i]:.1f}")
    
