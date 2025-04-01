raio = int(input("Digite o raio da circuferência: "))

if raio<=0:
    print("Raio inválido")
else:
    area = (raio*raio)*3.14
    print("A área da circuferência é: ", area)