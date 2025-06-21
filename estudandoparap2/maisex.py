cidades = ('Três Lagoas', 'Belo Horizonte', 'Rio de Janeiro', 'Piracicaba')

while True: 
    cidade_user = input("Digite o nome de uma cidade, digite 0 para sair: ")

    if cidade_user == 0:
        break
        
    for i in cidades:
        if i.lower() == cidade_user.lower():
            print(f" A cidade {cidade_user} está na tupla!")
        else:
            print(f"A cidade {cidade_user} não está na tupla")
    
    resposta = input("Deseja adicionar uma cidade na tupla? Digite sim ou não: ").lower()
    
    if resposta=='sim':
        cidades = list(cidades)
        adicionar = input("Digite qual cidade deseja adicionar: ")
        cidades.append(adicionar)
        cidades = set(cidades)
        cidades = tuple(cidades)
        for i in cidades:
            print(i)

        
        
    