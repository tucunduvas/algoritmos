
n = int(input("digite um número: "))

for x in range(n):
    for j in range(1,n+1):
        print(j, end="")
    print(" ")
    
print(" ") 

for l in range(n):
    for i in range(n,0,-1):
        print(i, end="")
    print(" ")

print(" ")
for w in range(1,n+1):
    for v in range(n+1,1,-1):
        print(w, end="")
    print(" ")

print(" ")

for c in range(n,0,-1):
    for b in range(1,n+1):
        print(c, end="")
    print(" ")
        
"""
PROVA

1 2 4 5 5.1 5.2 5.3 6.1 9 11 11.4 11.8 

calendario

fatoracao só com o for

mudar as orientaçãoes do exemplo 
1 2 3
1 2 3
1 2 3

3 2 1
3 2 1
3 2 1

3 3 3
2 2 2
1 1 1

1 1 1
2 2 2
3 3 3

1 2 3
2 1 3
2 3 1

num = (int(input("digite um numero: ")))
primo = 0
for i in range(2,num):
    if num%i==0:
        pass
    else:
        primo += 1
if primo>=1:
    print("é um número primo")  
else:
    print("não é um número primo")   

    

"""

#soma = soma + i

#soma += i

# i += 1 

num = int(input("Digite um número: "))
eh_primo = True

if num < 2:
    eh_primo = False
else:
    for i in range(2, num):
        if num % i == 0:
            eh_primo = False
            break

if eh_primo:
    print("É um número primo")
else:
    print("Não é um número primo")
