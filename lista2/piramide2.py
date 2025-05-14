x = int(input("Digite um número: "))

for i in range(1,x):
    for j in range(1,x-i):
        print(end=" ")
    for s in range(1,i+1):
        print(s,end="")
    for k in range(i-1,0,-1):
        print(k, end="")
    print(" ")