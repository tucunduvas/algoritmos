"""
    12. Leia 5 numeros do usuario e verifique se cada um deles e maior que 10
"""

i = 0
while i<5:
    num = int(input("Digite um número: "))
    if num>10: 
        print("O número foi aceito")
        i+=1
    else:
        print("O número não foi aceito")