
"""
Exercício 4: Fatoração em Números Primos
Receba um número inteiro n maior que 1 e, utilizando apenas laços de repetição, apresente
sua fatoração em números primos.
Exemplo para n = 60:
2 * 2 * 3 * 5

"""
n = int(input("digite um número: "))
fatoracao = 1
for i in range(n):
    if n%2==0:
        divisao = n/2
        fatoracao = fatoracao*2
        while divisao%2==0:
            divisao = divisao/2
            fatoracao = fatoracao*2
    if i%3 == 0:
        fatoracao = fatoracao*3
        divisao3 = n/3
        while divisao3%3==0:
            divisao3 = divisao3/3
            fatoracao = fatoracao*3
    if i%5==0:
        fatoracao = fatoracao*5
        divisao5 = n/5
        while divisao3%5==0:
            divisao5 = divisao5/5
            fatoracao = fatoracao*5
    if i%7==0:
        fatoracao = fatoracao*7
        divisao7 = n/7
        while divisao7%7==0:
            divisao7 = divisao7/7
            fatoracao = fatoracao*7
    if i%9==0:
        fatoracao = fatoracao*9
        divisao9 = n/9
        while divisao9%9==0:
            divisao9 = divisao9/9
            fatoracao = fatoracao*9
    if i%11==0:
        fatoracao = fatoracao*11
        divisao11 = n/3
        while divisao11%11==0:
            divisao11 = divisao11/11
            fatoracao = fatoracao*11
        
print(fatoracao)
            