num = int(input("Digite um número: "))
divisor = 0
for i in range(1,num):
    if num%i==0:
        divisor = divisor+i
if divisor==num:
    print(f"O número {num} é um número perfeito")
else:
    print(f"O numero {num} não é um número perfeito")
