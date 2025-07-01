"""
    Parte 2 — *args e **kwargs
A1. Soma com *args
Escreva uma funcao que aceita qualquer quantidade de argumentos num´ericos e
retorna a soma deles.
A2. Multiplica¸c˜ao com *args e verifica¸c˜ao de tipo
Crie uma fun¸c˜ao que multiplica todos os argumentos num´ericos, ignorando qualquer
argumento que n˜ao seja int ou float.
A3. Saudacao personalizada com **kwargs
Crie uma funcao saudar(**kwargs) que aceita os argumentos nome, idade e cidade,
e monta uma mensagem personalizada.
Exemplo: "Ola, Joao de 30 anos, morador de Sao Paulo!"
1
A4. Fun¸c˜ao de filtro com *args e **kwargs
Escreva uma fun¸c˜ao que aceita uma lista de n´umeros via *args e usa **kwargs para
aplicar filtros, como min=10, max=50.

"""

def soma(*args): 
    somaa = 0
    for arg in args:
        somaa += arg
    return somaa

print(soma(1,2,3,4))

def mult(*args):
# A2. Multiplicacao com *args e verificacao de tipo
# Crie uma funcao que multiplica todos os argumentos numericos, ignorando qualquer
# argumento que nao seja int ou float.
    multi = 1
    for arg in args:
        if isinstance(arg, int) or isinstance(arg, float):
            multi *= arg
        
    return multi

print(mult(2.5,3))


# A3. Saudacao personalizada com **kwargs
# Crie uma funcao saudar(**kwargs) que aceita os argumentos nome, idade e cidade,
# e monta uma mensagem personalizada.
# Exemplo: "Ola, Joao de 30 anos, morador de Sao Paulo!"
def saudacao(**kwargs):
    lista = list(kwargs.values())
    print(f"Ola, {lista[0]} de {lista[1]}, morador de {lista[2]}!")
saudacao(a= 'Gabi',b= 18, c='Castilho')
    

# A4. Fun¸c˜ao de filtro com *args e **kwargs
# Escreva uma fun¸c˜ao que aceita uma lista de n´umeros via *args e usa **kwargs para
# aplicar filtros, como min=10, max=50.

def lista_filtro(*args, **kwargs):
    minimo = kwargs.get('min')
    maximo = kwargs.get('max')
    return list(filter(lambda x: x if maximo>x>minimo else "", args))
    
print(lista_filtro(1,2,3,4,5,6,7,8,9,10, min=2, max=8))

