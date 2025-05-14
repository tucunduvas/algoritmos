import random

"""
LISTA 
TUPLAS 

DICIONÁRIOS 

LISTAS:
coleções heterogêneas de objetos 
podem ser qualquer tipo
pode ter outras listas dentro de listas 
[0, 1, "beto", [oi, tchau]]
listas são mutáveis 
sempre começa em 0 
"""

notas = [10,23,14]

print(notas)

nome = "beto"
print(nome[0])

print(len(nome)) #len é uma função que retorna o tamanho de uma coleção

#array é uma listas de listas
# porque uma string é uma lista 

nomes = ['gabriela', 'maria', 'vini'] 

nomes[2] = 'ana clara'

print(nomes[1]) 

for i in range(len(nomes)):
    print(nomes[i])

# segunda forma 

for nome in nomes:
    print(nome)
    
nomes.append('carol')
# -1 é a ultima posição de uma lista 
# -2 é a penultima
print(nomes[-1])

#ordernar 
"""
nomes.sort()

#inverter

nomes.reverse()

#remover pesquisar 

nome.insert(2,"corsa")
print(nome)

#remove

nome.remove("toyota")

#sort / ordena em ordem ascendente 

nome.sort()
print(nome)

#pop exclui um item específico e retorna o valor, se não tiver nada no () ele exclui o ultimo

nome_removido = nome.pop(2)
print(nome_removido)

"""


posicao = 0
for n in nomes:
    print(f"Posição {posicao}, elemento: {n}")
    posicao +=1
    
for i,n in enumerate(nomes):
    print(f"Posição{i} elemento = {n}")
    
#dada as listas [a,b,c] e [d,f,g] como poderiamos juntar?

listaA = ['A', 'B', 'C']
listaB = ['D', 'F', 'G']

listaA.append(listaB)

print(" ")
print(listaA)

# PESQUISAR
# ZIP 

for l in listaA:
    print(l)
    
l1 = ["arroz", "feijao", "batata"]



for l in l1:
    for letra in l:
        print(letra)

#enumerate 
#  retorna uma tupla de dois elementos a cada iteracao

musicas = ['meu lugar', 'nettie']
cantores = ['arlindo cruz', 'type o negative']

musicas += cantores

"""
for m in musicas:
    print(m)
    for c in cantores:
        musicas.append(c)
"""
i = 0
tamanho = len(cantores)
for m in musicas:
    while i<tamanho:
        for c in cantores:
            musicas.append(c)
        i +=1

print(musicas)

#pensando em listas de 50 alunos, onde serão lidos (random) 4 notas(0-100)
#mostre a porcentagem de alunos aprovados e reprovados
# imprima os 5 primeiros alunos com media mais alta 
# imprima os 5 piores
# imprima a nota mais alta, a posicao e a qual aluno pertence 

x = random.randint(0,100)

#TUPLAS 

#tuplas são imutáveis 
# não é possivel:
# remover
# acrescentar
# apagar

tupla = (1, 2, 3, 4)

print(tupla[0])

tupla.count()
tupla.index()
#tupla de unico elemento

unica = (3, )

# o que define uma tupla é a virgula e nao os parenteses 


#converter tupla em lista 
listar = list(tupla)

# da pra fazer uma tupla de listas 
lista_de_tupla = ([1,2,3], [3,4], [5, 6])


#transformar uma lista em tupla
lista5 = ['computador', 'gato']
lista_em_tupla = tuple(lista5)

#PESQUISA
# SET, MUTAVEL? IMUTAVEL? COMO APLICAR, COMO USAR
# FRONZENSET, MUTAVEL? TUDO O QUE É PRECISO SABER 
# UNIÃO INTERSECÇÃO E DIFERENÇA DE LISTAS (TUPLAS TB?)

# O QUE É RANGE?  RANGE É UMA FUNÇÃO, PODE SER LISTA? TUPLAS 








