alunos = {'gabriela': [10,9,8], 'maria': [10,7,6], 'ana': [5,4,7], 'vini': [8,3,4]}

        
def ler_opcao(qntd):
        try:
            opcao =  int(input("Digite a opc: "))
            if 0<=opcao<=qntd:
                return opcao
        except ValueError:
            print("Invalido")
            

def add(nome):
    nota = float(input(f"Digite a nota que deseja adicionar para o aluno {nome}: "))
    alunos[nome].append(nota)
            
            
while True:
    while True: 
        print("Deseja adicionar um novo aluno?: ")
        print(" 1 - sim")
        print(" 2 - sair")
        opcao = ler_opcao(2)
        
        if opcao == 2:
            break
        notas = []
        if opcao==1:
            novo = input("Digite o nome do novo aluno: ")
            for i in range(3):
                nota = float(input(f"digite uma nota do aluno {novo}: "))
                notas.append(nota)
                alunos[novo] = notas
    while True:
        print("Deseja adicionar uma nota a um aluno existente? ")
        print("1 - sim ")
        print("2 - sair")
        opcao = ler_opcao(2)
        
        if opcao==1:
            print("de qual aluno deseja adicionar: ")
            nomes = list(alunos.keys())
            for i,j in enumerate(nomes):
                print(f"{i} - {j}")
            opcao = ler_opcao(len(nomes)-1)
            nome = nomes[opcao]
            add(nome)
        if opcao==2:
            break
        
    for i in alunos.values():
        soma = 0
        for x in i:
            soma += x
            media = soma/len(i)    
            print(f' média {i} {media}')    
        for j in alunos.keys:
            
        
        