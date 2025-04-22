num = int(input("Digite um número: "))

anterior = 0
proximo = 1
atual = 1
fibonacci = [0,1,1]
lista=[]

for i in range(1,num):
    print(proximo)
    proximo = atual + anterior
    anterior = atual
    atual = proximo
    
num = int(input("Digite um número: "))

fibonacci = [0, 1]  

for i in range(2, num): 
    proximo = fibonacci[-1] + fibonacci[-2] # -1 exibe o ultimo numero adicionado da lista, -2 exibe o penultimo adicionado  
    fibonacci.append(proximo)

for i in range(1, num):
    print(fibonacci.reversed())

"""
Dentro do loop:

Some os dois últimos números para obter o próximo da sequência.

Atualize os dois últimos valores com os mais recentes.

Armazene ou exiba o novo número gerado.
        
for i in range(1,num):

for i in range(num,0):
    seq2 = i-1
    seq1 = seq2-1
    fibonacci = seq2 + seq1
    print(fibonacci)

"""
