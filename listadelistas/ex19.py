# 19. Solicite nomes at´e que o usu´ario digite ”sair”. Armazene em uma lista e imprima.
lista = list()
while True:
    nomes = input("Digite um nome: ").lower()
    lista.append(nomes)
    if nomes=='sair':
        break
    
sair = nomes.pop(-1)
print(nomes)
    