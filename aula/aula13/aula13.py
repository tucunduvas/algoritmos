#RECURSIVIDADE 

#uma técnica de computação onde uma função 'chama a si mesma' para resolver algum problema

"""
    Principais características:
    1 caso base:
    condição de parada que evita chamadas infinitas 
    
    2 caso recursivo
    onde a funcao 'chama a si mesma' com um problema menor
"""

def func(x):
    print(x)
    #caso base:
    #quando x for -1 vai parar
    if x <1:
        return
    func(x-1)
    
    
func(10)

########

def func(x):
    #caso base:
    #quando x for -1 vai parar
    if x <1:
        return 0
    print(x)
    return x + func(x-1)
    
    
print("funcao",func(10))

# 3 + func(2)
# 2 + func(1)
# 1 + func(0)

#fatorial de 5 

def fatorial(x):
    if x==1:
        return 1
    print(x)
    return x*fatorial(x-1)

print(f"Fatorial: {fatorial(5)}")

# fibonacci

def fibonacci2(y):
    if y==1:
        return 1
    y - (y-1)

    
    
print("fibo", fibonacci2(7))
"""
    7
    6
    5
    4
    3
    2
    1
    1+2 = 3
    3+2 = 5 
    5+3 = 8 
    5 + 8 + 13 
"""
# num = int(input("Digite um número: "))

# anterior = 0
# proximo = 1
# atual = 1

# #()reversed
# for i in range(num-1,-1,-1):
#     for x in range(1,i):
#         proximo = atual + anterior
#         anterior = atual
#         atual = proximo
#     print(proximo)
#     anterior = 0
#     proximo = 1
#     atual = 1


def fibonacci(y):
    atual = fibonacci(1)
    prox = atual + fibonacci(1)
    anterior = atual
    print(prox)
    return

def fibo(n):
    if n<=1:
        return n
    return fibo(n-1) + fibo(n-2)

print(fibo(7))
