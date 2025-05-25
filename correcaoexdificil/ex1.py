passos = int(input("digite quantos passos: "))

pedra = 0
buraco = 0
for i in range(1,passos+1):
        obstaculo = input("Você encontrou uma pedra ou um buraco? Responda com P ou B: ").upper()
        if obstaculo== 'P':
            pedra +=1
        elif obstaculo == 'B':
            buraco +=1
        else:
            while obstaculo != 'P' or obstaculo != 'B':
                obstaculo = input("Você encontrou uma pedra ou um buraco? Responda com P ou B: ").upper()
        
if buraco>pedra:
    print("Cuidado! mais buracos")
print(f"Foram encontrados {buraco} buracos")
print(f"Foram encontrados {pedra} pedras ")