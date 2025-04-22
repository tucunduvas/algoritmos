n = int(input("Digite um número: "))

numerador = 0
denominador = 0
resultado  = 0
for i in range(0,n):
    numerador = i+1
    denominador = numerador*2-1
    fracao = numerador/denominador
    print(fracao)
    resultado = resultado + fracao
    
    
print(f"O resultado da série é: {resultado}")