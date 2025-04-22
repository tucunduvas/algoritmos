import math

numero = float(input("Digite um número: "))

raiz_quadrada = math.sqrt(numero)

numero_raizquadrada = int(raiz_quadrada)

if numero_raizquadrada*numero_raizquadrada == numero:
    print(f"O número {numero} é um quadrado perfeito")
else: 
    print(f"O número {numero} não é um quadrado perfeito.")