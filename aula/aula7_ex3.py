import random
from random import randint
# ex 3  crie um programa para ler o nome, matricula e as quatro notas de 5 alunos e armazene em um dic 
# use notas aleatorias e compreensao de listas 

# aluno = {matricula: nome, notas:[n1,n2,n3,n4]}
# aluno = {123: 'gabi', nota1: [1,2,3,4]}


# mostrar o aluno com a maior média
# mostrar a % de alunos com média maior que 8
# mostrar a % de alunos que estariam reprovados, a média é 4 

#treinar usar tuplas como chaves 

alunos = {}

for i in range(5):
        matricula = random.randint(100,500)
        nome_aluno = input("Digite o nome: ")
        notas = [0]*4
        for b in range(4): 
            notas[b] = random.randint(0,10)
        alunos[matricula] = {nome_aluno: notas}
        

#matricula é a chave de um dicionario, 
# o nome do aluno é o valor da matricula 
# e no nome cria outro dicionario que o valor é a nota 


resultado = {}
for i in alunos.values(): 
    for a in i.keys():
        for j in i.values():
            soma = 0
            media = 0
            for k in j:
                soma += k
                media = soma/4
                resultado[a] = media

for i in resultado.items():
    print(i)



qntd_maior8 = 0
for i in resultado.values():
    if i>8:
        qntd_maior8+=1
    
porcentagem1 = (qntd_maior8/5)*100


qntd_reprovados = 0
for i in resultado.values():
    if i<4:
        qntd_reprovados+=1

porcentagem2 = (qntd_reprovados/5)*100

maior_media = max(resultado.items())
print(f"O aluno com a maior média é: {maior_media}")
print(f"A porcentagem de alunos com  média maior que 8: {porcentagem1}%")
print(f"A porcentagem de alunos reprovados: {porcentagem2}%")

# o dic com nome e nota é o i 
# j é o a lista de nota
# k in j é o elementos da nota 
