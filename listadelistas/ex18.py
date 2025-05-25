"""
18. Verifique se o n´umero 7 est´a presente na lista [3, 6, 9, 12].
19. Solicite nomes at´e que o usu´ario digite ”sair”. Armazene em uma lista e imprima.
20. Crie uma lista de 5 letras e converta para uma ´unica string com join.


"""

lista = [3, 6, 9, 12]
sete = False

for elemento in lista: 
    if elemento == 7:
        sete = True

if sete: 
    print("O número 7 está na lista")
else:
    print("O número 7 não está na lista")


# outro jeito de fazer 
if 7 in lista:
    print("O número 7 está na lista")
else:
    print("O número 7 não está na lista")
    