i = 1

while i<6:
    senha = input("Digite a senha: ")
    if senha == 'Open123':
        print("Acesso concedido")
        senha = True
        break
    else: 
        print("senha incorrera")
        print(f"Voce tem {5-i} tentativas restantes")
    if i ==5:
        print("todas as tentativas foram usadas")
    i +=1
    
par = 0
impar = 0
numpar = 0
numimpar = 0
if senha == True:
    for i in range(1,11):
        num = int(input("digite 10 numeros secretos para continuar, eu informarei quantos sao pares, quantos sao impares e somarei os valores de cada grupo: "))
        if num%2==0:
            par += 1
            numpar += num
        else:
            impar+=1
            numimpar +=num
        
print(f"Pares: {par}")
print(f"Impares: {impar}")
print(f" Soma dos pares: {numpar}")
print(f" Soma dos impares: {numimpar}")
