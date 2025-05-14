i = 0
soma = 0
while True: 
    idade = int(input("Digite a idade: "))
    if idade> 0:
        i +=1
        soma += idade
    else:
        print("impossível calcular")
        break
    
media = soma/i
print(media)
    
    