num1 = int(input("Digite um número: "))
num2 = int(input("Digite um número: "))
num3 = int(input("Digite um número: "))

soma = num1+num2+num3

if soma==180:
    if num1==90 or num2==90 or num3==90:
        print("é um triângulo retângulo")
    elif num1<90 and num2<90 and num3<90:
        print("é um triângulo acutângulo")
    elif num1>90 or num2>90 or num3>90:
        print("é um triângulo obtusângulo")
else: 
    print("Não é um triângulo")