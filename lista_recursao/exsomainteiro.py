"""
Soma dos digitos de um nuumero
Escreva uma funcao recursiva que retorna a soma dos digitos de um nuumero inteiro
positivo.
Exemplo: soma digitos(1234) → 10

"""

def somarr(numero):
    numero = str(numero)
    if len(numero)<=1:
        return numero
    return int(numero[-1]) + int(numero[:-1])
somarr(1234)
    