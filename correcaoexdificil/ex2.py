negativo = 0
multiplo3 = 0

for i in range(1,8):
    num = int(input("Digite um número inteiro: "))
    if num%3==0:
        multiplo3 +=1
    if num<0:
        print("Alarme ativado, saia imediatamnete")
        break 
    
if multiplo3>=4:
    print("cofre aberto com sucesso!")
else: 
    print("tentativa falhou. o cofre permanece fechado ")