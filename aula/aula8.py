lista = [1,2,3,4,5]

# map, filder, reduce (prox conteúdo) (estudar)

#convencao de lista 

quadrado = [num**2 for num in lista]
print(quadrado)

pares = [num%2==0 for num in lista]
print(pares)

par = [num for num in lista if num%2==0]
print(par)

def somar(x,y):
    soma = x+y
    return print(soma)
    # ou return print(x+y)

somar(40,60)

#ou 


def somar(x,y): 
    return x+y, x, y

print(somar(50,60))


def adicao(x,y): 
    return x+y,

resultado = print(adicao(3,2)) 

# SE SÓ QUISER MOSTRAR:
# o ideal é nao por direto o print na funcao sem return EXEMPLO PRINT
# com return o ideal é armazenar uma variavel para ultilizar o resultado depois em outras operacoes

# EXEMPLO PRINT 
def adicaoo(x,y): 
    print(x+y)

adicaoo(1,1)


#para casos em que sabe que precisa da funcao mas nao sabe o que ela vai fazer mas ela deve existir
def funcao():
    pass

#procedure 

def subtracao(x,y):
    return x-y

resultado = subtracao(5,1)
print(resultado)

def divisao(x,y):
    return x/y

resultadodivisao = divisao(6,2)
print(resultado)

def potencia(x,y):
    print(x**y)
    
potencia(3,2)


