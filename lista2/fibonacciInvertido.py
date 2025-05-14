num = int(input("Digite um número: "))

anterior = 0
proximo = 1
atual = 1

#()reversed
for i in range(num-1,-1,-1):
    for x in range(1,i):
        proximo = atual + anterior
        anterior = atual
        atual = proximo
    print(proximo)
    anterior = 0
    proximo = 1
    atual = 1
    