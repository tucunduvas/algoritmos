"""
    Exercício 6: Série Harmônica Alternada
Utilizando apenas laços de repetição, calcule a soma dos primeiros n termos da série
harmônica alternada:
* Uma série harmônica é uma série infinita em matemática, formada pela soma dos inversos
dos números naturais consecutivos

"""
#serie harmonica sempre comeca positivia
#ou seja, uma serie alteranda contem todos os impares positivos e todos os pares negativos
n = int(input("Digite um número: "))
soma = 0
for i in range(1,n+1):
    serie = 1/i
    if i%2!=0:
        soma = soma + serie
    else:
        soma = soma - serie

print(f"A soma da série harmônica alterada é: {soma}")