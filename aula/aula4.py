"""
1 variavel de controle
2 condição de parada
3 atualização da variavel de controle

"""
#var de controle
i = 0
while i<10:
    if i%2==0:   
        print(f"i = {i}")
    i =i+ 1 #incremento

# cirar um lacp de repeticao com um while que dependa da resposta do user para continuar o laço

resp = 's'
while resp=='s': 
    print("ainda estou repetindo")
    while True: 
        resp = input("deseja continuar? (s) ou (n) ").lower()
        if resp=='s' or resp=='n':
            break
    
print("Termineiii!!!!!")

# .upper para deixar tudo maisculo 

