import math

"""
Lambda function

funcoes anonimas, não precisam de nome

def soma(a,b):
    return a+b

sintaxe básica

lambda argumentos: expressao

"""

dobro = lambda x: x*2

print('Exemplo - dobro de 5: ', dobro(5))

soma = lambda x,y: x+y

print('soma de 3 e 4: ', soma(3,4))

# h2 = a2 + b2

hipotenusa = lambda x,y: (x**2+y**2)**0.5

hipotenusa = lambda x,y: math.sqrt(x**2+y**2)

print("A hipotenusa é: ", hipotenusa(6,8))

# filter, map

numeros = [1,2,3,4,5,6,7,8,9,10]

# iteira todos os elementos do array, o x da lambda é cada elemento
pares = list(filter(lambda x: x%2==0, numeros))
print("Exemplo 3 - números pares", pares)


