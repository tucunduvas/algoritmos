
""" 
Exercício 1 - Soma dos números inteiros 
Faça um programa usando laços que some todos os números inteiros de 1 até n fornecido 
pelo usuário. 
Exemplo: 
Entrada: 5 
Saída: 15 

Exercício 2 - Tabela de Multiplicação
Faça um programa que exiba a tabuada de multiplicação do número fornecido pelo usuário
(de 1 a 10).

Exercício 3 - Contagem Regressiva
Crie um programa que faça uma contagem regressiva, do número fornecido até 0, utilizando
laços de repetição.

Exercício 4 - Números Pares até N
Crie um programa que imprima todos os números pares até o número fornecido pelo
usuário usando laços.

Exercício 5 - Somatório dos Ímpares
"""

n = int(input("Digite um número: "))
n = n+1
soma = 0 
for i in range(0,n):
    soma = soma+i

print(soma)

num = int(input("Digite um número: "))
for i in range(0,11):
    print(f"{num}x{i}=",(num*i))
    

contagem = int(input("Digite um número: "))

for i in range(contagem, 0, -1):
    print("Falta", i)
    
x = int(input("Digite um número: "))

for i in range(0,x):
    if i%2==0:
        print(f"Os números pares são: ", i)
        
a = int(input("Digite um número: "))       

soma = 0
if a>0:
    for i in range(0,a):
        if i%2!=0:
            soma=soma + i
    print(f"A soma dos números ímpares é {soma}")
else:
    print("Não é um número inteiro positivo")  
    

numero = int(input("Digite um número: "))
numero=numero+1
fatorial=1
if numero>0:
    for i in range(1,numero):
        fatorial = fatorial*i
        print(fatorial)
else: 
    print("Não é um número inteiro positivo")


g = int(input("Digite um número: "))
if g>0:
    for i in range(1,g):
        if g%i==0:
            print(f"{i} é um divisor inteiro de {g}")

f = int(input("Digite um número: "))
f = f+2 
for i in range(f):
    for z in range(1,i):
        print(z, end=" ")
    print(" ")

frase = input("Digite uma frase: ").lower()
vogal = " "
vogais = 0
for i in frase:
    vogal=i
    if vogal=="i":
        vogais+=1
    if vogal=="a":
        vogais+=1
    if vogal=="e":
        vogais+=1
    if vogal=="o":
        vogais+=1
    if vogal=="u":
        vogais+=1
        
print(f"A frase {frase} têm {vogais} vogais")

num = int(input("Digite um número: "))
divisor = 0
for i in range(0,num):
    if num%i==0:
        divisor = divisor+i
if divisor==num:
    print(f"O número {num} é um número perfeito")
else:
    print(f"O numero {num} não é um número perfeito")

"""
Exercício 2: Número Perfeito
Faça um programa usando apenas laços que determine se um número informado pelo
usuário é um número perfeito. Um número é perfeito quando é igual à soma dos seus
divisores próprios (exceto ele mesmo).
Exemplo:
Entrada:
6
Saída:
Número Perfeito
"""