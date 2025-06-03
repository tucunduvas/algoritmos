def divisao(x,y):
    if y>0:
        resultado = x/y
        print(resultado)
    else:
        print("não é possível dividir por 0")
        
def divisao(x,y):
    if y>0:
        return x/y
    print("não é possível dividir por 0")
# nao pode digitar 0 

#escopos globais devem ser evitados 

#garbage colector 

def somar(x,y): 
    return x+y, x, y
x = somar(50,60)
print(x)


def potencia(x,y):
    print(x**y)
    
quadrado = potencia(3,2)

def func1(x,y):
    h = [x**2 for x in func2(y)]
    return h

def func2(x):
    r = []
    for i in func3(x, x*2,  x*3): 
        r.append(i**0.5)
    return r
        
def func3(a,b,c):
    lista = [x**2 for x in [a,b,c] if x%3 == 0]
    return lista

print(func1(2,3))






