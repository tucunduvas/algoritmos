"""

Contagem regressiva com atraso
Implemente uma funcao recursiva contagem regressiva(n) 
que imprime uma contagem de n ate 0. Ao chegar a 0, deve imprimir "Boom!".

(Opcional: usar time.sleep(1) para simular contagem real.)

"""

def contagem(n):
    if n==-1:
        return 1
    print(n)
    if n == 0:
        print("Boom!")
    return n - contagem(n-1)

contagem(5)