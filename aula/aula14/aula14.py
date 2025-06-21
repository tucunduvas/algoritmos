""" 

"""
# b é um parametro opcional, 
#parametros opcionais sempre vem por ultimo

from functools import reduce


def adicao(a, b=1):
    print("adição: ", a+b)
    
adicao(8)


#args abreviações para um número específico de argumentos
#sãoo convenções em python, permitem que funções recebam um número variável de parametros 

def soma(*args):
    pass

# def funcao(a,b,*args):
#     print(f"Argumentos recebidos: {args}")
#     for arg in args:
#             print(f"- {arg}")
            
# funcao(2,3,5,6,[1,3,4],[2,3,[1,2,3]])

            
#funcao para contar o número de sublistas em uma lista: usar isistance 
def funcao(a,b,*args):
    contador = 0
    for arg in args:
        if isinstance(arg, list): 
            for i in arg: 
                if isinstance(i, list): 
                    contador+=1
    print(contador)

funcao(2,3,5,6,[1,3,4],[2,3,[1,2,3], [2,4], [3,4]])

def recursao(*args):
    contador = 0
    for arg in args:
        if isinstance(arg, list):
            contador += 1 + recursao(*arg)
    return contador


print(recursao(2,3,5,6,[1,3,4],[2,3,[1,2,3], [2,4], [3,4]]))
    
def usando_reduce(*args):
    return reduce(lambda count, item: count + 
            (1 if isinstance(item, list) else 0), args)

print(usando_reduce(1,2,[1,1],[6,6]))
#fazer com reduce e recursao



# lista = [2,3,4,5,6,[1,2,3],[4,5,[6,7]]]
# print(f"sublistas diretas: {}")

# def soma(a,b,c):
#     pass

# soma(c=2,a=6, b=4)

def funcao_completa(param_obg, *args, **kwargs):
    print(f"parametro obrigatório: {param_obg}")
    print(f"argumentos extras: {args}")
    print(f"Kwargs: {kwargs}")
    
funcao_completa("Valor1", "extra1", "e2", "e3", nome = "beto", idade=30)

""" 
implemente uma calculadora que leia 2 tipos (soma, mult), lista de numeros, parametro nomeado para exibir detalhes ou nao, exibir_detalhes = true
"""

def calculadora():
    pass