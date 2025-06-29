def inverso(resultado):
    if resultado == ''.join(reversed(resultado)):
        return resultado
    resultado = list(resultado)
    k = 0
    for i in resultado:
        k+=1
        resultado[-k] = inverso(resultado)
        
#  Inverter string recursivamente
# Escreva uma fun¸c˜ao recursiva que recebe uma string e retorna a string invertida.
# Exemplo: "python" → "nohtyp"

def fatorial(x):
    if x==1:
        return 1
    print(x)
    return x*fatorial(x-1)

print(f"Fatorial: {fatorial(5)}")