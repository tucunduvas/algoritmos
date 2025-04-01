num1 = int(input("digite um número: "))
num2 = int(input("digite um número: "))
num3 = int(input("digite um número: "))
num4 = int(input("digite um número: "))
soma = 0 

if num1%2==0:
    soma = soma + num1
else:
    soma = soma

if num2%2==0:
    soma = soma + num2
else:
    soma = soma

if num3%2==0:
    soma = soma + num3
else:
    soma = soma

if num4%2==0:
    soma = soma + num4
else:
    soma = soma

print("A soma dos números pares é: ", soma)


