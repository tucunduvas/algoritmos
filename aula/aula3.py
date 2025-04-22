#for
    
#while

#do while

"""
variavel de controle: contador
condição de parada 
atualização da variável de controle
"""

for i in (1,2,3,4,5,6,7,8,9):
    print(i)
    
for i in (1,2,3,4,10,6,7,8,9):
    print(i)
    
for i in (range(10)): #o valor da range não é escrito, vai parar no 9
    print(i)
    

for i in (range(1)):
    n1 = float(input("Digite a nota 1: "))
    n2 = float(input("Digite a nota 2: "))
    n3 = float(input("Digite a nota 3: "))
    n4 = float(input("Digite a nota 4: "))
    media = (n1+n2+n3+n4)/4
    print(media)
    print("Próximo aluno ->")

print("Oi")   
for i in (range(2,20, 3)): #o terceiro número quer dizer que vai de 3 em 3 
    print(i)
    

for i in (range(20,0,-1)):
    print(i)
    
