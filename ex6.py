num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

print("o n1 é: ", num1)
print("o n2 é: ", num2)

if num1>0 and num2>0:
    troca = num2
    num2 = num1
    num1 = troca
    print("Troca de valores:")
    print("o n1 é: ", num1)
    print("o n2 é: ", num2)
else:
    print("os números devem ser maiores que 0")

    
    