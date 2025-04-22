num = int(input("Digite um número: "))
num = num+1
for i in range(num,0,-1):
    for j in range(1,i):
        print(j, end=" ")
    print(" ")