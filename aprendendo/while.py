num=int(input("Digite um número: "))

soma = 0
while num!= 0:
    soma =soma + num
    num= int(input("Digite outro número: "))

print(soma)

"""
Leia uma quantidade indeterminada de duplas de valores inteiros X e Y. Escreva para cada X e Y uma
mensagem que indique se estes valores foram digitados em ordem crescente ou decrescente. O
programa deve finalizar quando forem digitados dois valores iguais. 

"""
x = int(input("Digite o x: "))
y = int(input("Digite o y: "))

while x !=  y:
    if x<y:
        print(f"O x {x} e o y {y} foram digitados em ordem crescente")
    else: 
        print(f"O x {x} e o y {y} foram digitados em ordem decrescente")
    x = int(input("Digite o x: "))
    y = int(input("Digite o y: "))