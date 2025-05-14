"""_summary_

Exercício 5: Diamante de caracteres ASCII
Utilizando apenas laços de repetição, imprima um diamante formado por caracteres ASCII
sequenciais (começando em "A"), com altura ímpar informada pelo usuário.
Exemplo para altura 5:
A    
ABA
ABCBA
ABA
A


"""




x = int(input("Digite um número: "))

for i in range(1,x):
    for j in range(1,x-i):
        print(end=" ")
    for s in range(1,i+1):
        print((chr=),end="")
    for k in range(i-1,0,-1):
        print(k, end="")
    print(" ")