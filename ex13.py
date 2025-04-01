num1 = int(input("Digite um número: "))
num2 = int(input("Digite um número: "))
num3 = int(input("Digite um número: "))
num4 = int(input("Digite um número: "))
num5 = int(input("Digite um número: "))

media = 0
qtde = 0

if num1%2!=0:
    media = media + num1
    qtde = qtde + 1 
else: 
    media = media 

if num2%2!=0:
    media = media + num2
    qtde = qtde + 1  
else: 
   media = media

if num3%2!=0:
    media = media + num3
    qtde = qtde + 1  
else: 
   media = media

if num4%2!=0:
    media = media + num4
    qtde = qtde + 1 
else: 
   media = media

if num5%2!=0:
    media = media + num5
    qtde = qtde + 1 
else: 
    media = media

resultado = media/qtde

print(resultado)

