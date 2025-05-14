n = int(input("Digite um número: "))        

primo = [2,3]

for i in range(4,n):
    if (i%2!=0 and i%3!=0 and i%5!=0 and i%7!=0):
        primo.append(i)
    else:
        pass
    
for j in primo:
    gemeo = j+2
    if gemeo in primo: 
        print(j,gemeo)