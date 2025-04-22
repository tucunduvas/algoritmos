        
a = int(input("Digite um número: "))       

soma = 0
if a>0:
    for i in range(0,a):
        if i%2!=0:
            soma=soma + i
    print(f"A soma dos números ímpares é {soma}")
else:
    print("Não é um número inteiro positivo")  