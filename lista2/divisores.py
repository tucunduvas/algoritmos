g = int(input("Digite um número: "))
divisores = 0
if g>0:
    for i in range(1,g+1):
        if g%i==0:
            print(f"{i} é um divisor inteiro de {g}")
            divisores = divisores+1

print(f"O número {g} tem {divisores} divisores.")