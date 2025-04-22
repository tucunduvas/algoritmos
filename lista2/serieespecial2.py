n = int(input("Digite um número: "))

numerador = 0
denominador = 0
resultado  = 0

for i in range(0,n):
    if numerador<n:
        numerador = numerador+ 1
        denominador = numerador*2-1
        
        fracao = numerador/denominador
        resultado = resultado + fracao
    else:
        break
    if numerador<n:      
        numerador = numerador+1
        denominador = denominador+2
        fracao = numerador/denominador
        resultado = resultado - fracao 
    else:
        break
print(f"O resultado da série é: {resultado}")        