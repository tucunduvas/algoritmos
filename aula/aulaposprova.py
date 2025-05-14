passos = int(input("quantos passos o astronauta deu: "))

pedras = 0
buracos = 0

for i in range(passos+1):
    obs = input(f"Passo {i}: Pedra (P) ou buraco (B)?: ").upper()
    
    if obs == 'P':
        pedras += 1
    elif obs == 'B':
        pedras +=1
    else:
        print("letra inválida")
        
print(f"total de pedra {pedras}")
print(f"total de buracos {buracos}")

if buracos>pedras:
    print("Cuidado! Mais buracos do que pedra")
    
eq = 0
ins = 0

for i in range(8):
    num = int(input("Digite um número inteiro: "))
    if (num%2==0 and num%5==0) and (num%2!=0 and num%3==0):
        eq+=1
    else:
        