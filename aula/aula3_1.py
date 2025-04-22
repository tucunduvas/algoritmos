"""
ler dos números
o primeiro vai ser o inicio do laco
o segundo é o fim 
"""

inicio = int(input("Digite o início do laço: "))
fim = int(input("Digite o fim do laço: "))

if inicio<fim:
    for i in (range(inicio,fim)):
        print(i)
else: 
    aux = fim
    fim = inicio
    inicio = aux 
    for i in (range(inicio,fim)):
        print(i)
        
"""
outro jeito de fazer: 

if inicio<fim:
    for i in (range(inicio,fim)):
        print(i)
else:  
    for i in (range(fim,inicio)):
        print(i)
"""

"""
segundo ex
*
**
***
****
*****
"""

i = 1 

while i<=5:
    print("*")
    i = i+1
