num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
mdc = 0
if num1<num2:
    for i in range(1,num2):
        if num1%i==0 and num2%i==0:
            mdc = i       
else: 
    for i in range(1,num1):
        if num1%i==0 and num2%i==0:
            mdc = i
print(f"O máximo divisor comum de {num1} e {num2} é {mdc}")