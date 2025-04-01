num1 = int(input("Digite um número: "))
num2 = int(input("Digite um número: "))
num3 = int(input("Digite um número: "))

if num1==num2==num3:
    print("equilátero")
elif num1!=num2==num3 or num1==num2!=num3 or num1==num3!=num2:
    print("isósceles")
elif num1!=num2!=num3:
    print("escaleno")
