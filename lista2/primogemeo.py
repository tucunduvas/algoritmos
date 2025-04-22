n = int(input("Digite um número: "))
            
for i in range(1,n):
    for x in range(2,i-1):    
        if i%2!=0 and i%3!=0:
            primo = i
            gemeo = i+2
            if gemeo%2!=0 and i%3!=0:
                print(f"{primo},{gemeo}", end="")
            
primo = [1,2,3]
for i in range(1,n):
    for x in range(2,i-1):
        if i%x!=0 and i%2!=0 and i%3!=0:
            primo.append(i)
                
for j in primo:
    gemeo = j+2
    if gemeo in primo: 
        print(j,gemeo)
        
primo = [1,2,3]
for i in range(1,n):
    for x in range(2,i-1):
        if i%x!=0 and i%2!=0 and i%3!=0:
            primo.append(i)
    print(primo)   
    for j in primo:
                gemeo = j+2
                if gemeo in primo: 
                    print(j,gemeo)
            
"""
primo = ""

for i in range(1,n):
    for x in range(2,i-1):
        if i%2!=0 and i%3!=0 and i%5!=0:
            primo = i
    print(primo, end=)


"""
"""   
Exercício 3: Números Primos Gêmeos
Imprima todos os pares de números primos gêmeos até um limite n utilizando
exclusivamente laços de repetição. Números primos gêmeos são primos cuja diferença é
exatamente 2.
Exemplo para n = 20:
(3, 5), (5, 7), (11, 13), (17, 19)
"""
                    




