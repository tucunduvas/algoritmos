from random import randint
import random
"""

dicionários   

- uma lista de associações compostas por uma chave unica 
- são mutáveis
- nao são ordernados
sintaxe 

tupla e lista não pode ser chaves

chaves sao imutaveis - qualquer elemento que é imutável pode ser chave 

retornou uma lista de tuplas 
"""

dicionario = {'a': 1, 'b': 'beto'}

dicionario = {'a': [2,3], 'b': (1,2,[1,2,{1:20,2:30}])}

dic = {'nome1': 'Beto', 'nome2':'Ana', 'nome3': 'Vitor'}

dic['nota'] = 7.80 

#usando para debug 
print(dic)

itens = dic.items()
chaves = dic.keys()
valores = dic.values()

print(f"Itens = {itens}")
print(f"Chave = {chaves}")
print(f"Valores = {valores}")

for i in dic.items():
    print(i)
    
for i,j in dic.items():
    print(f'i={i}, j={j}')
    
for i in dic.keys():
    print(i)
    
for j in dic.values():
    print(j)
    
print(dic["nome1"]) #retorna o valor, no caso Beto

#leiam o nome de 5 pessoas e armazena em um dicionário
nomes = {}
for i in range(5):
    n = input("Digite um nome: ")
    nomes[i] = n

print(nomes)

# crie um programa para gerar um dic com 20 numeros inteiros mostre a soma de todos os elementos

oi = random.randint(5,30)

num = {}
for i in range(20):
    valor = random.randint(1,100)
    num[i] = valor
    #chave [posicao] = valor
    
sum_valores = sum(num.values())

print(sum_valores)

soma =0
#poderia ir somando direto no laço de rep
for i in range(20):
    valor = random.randint(1,100)
    num[i] = valor
    soma += num.get(i)

#compreensao de  listas 

lista = [i for i in range(5)]  # [0,1,2,3,4]

print(lista)

for i in [0.2, 0.3, 0.4]:
    pass 

#PESQUISA 
# COMO TRABALHAR COMPREENSÃO DE LISTAS 
# 

#get busca um elemento pela chave

print(dic.get('nome1'))

#poderia ir somando direto no laço de rep
for i in range(20):
    valor = random.randint(1,100)
    num[i] = valor
    soma += num.get(i)
    
# ex 3  crie um programa para ler o nome, matricula e as quatro notas de 5 alunos e armazene em um dic 
# use notas aleatorias e compreensao de listas 

# aluno = {matricula: nome, notas:[n1,n2,n3,n4]}
# aluno = {123: 'gabi', nota1: [1,2,3,4]}

# aluno = {123: {'beto': [1,2,3,4,] }}

# mostrar o aluno com a maior média
# mostrar a % de alunos com média maior que 8
# mostrar a % de alunos que estariam reprovados, a média é 4 
alunos = {}
for i in range(5):
    nome_aluno = input("Digite o nome: ")
    alunos[f'nome{i}'] = nome_aluno

print(alunos)