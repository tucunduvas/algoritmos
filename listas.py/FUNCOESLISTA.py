
carros = ["hb20", "fusca", "toyota"]

print(carros[0])
print(carros[-1])

#append / adiciona um elemento no final da lista 

carros.append("fiat")

#insert / insere em uma posição específica da lista 

carros.insert(2,"corsa")
print(carros)

#remove

carros.remove("toyota")

#sort / ordena em ordem ascendente 

carros.sort()
print(carros)

#pop exclui um item específico e retorna o valor, se não tiver nada no () ele exclui o ultimo

carro_removido = carros.pop(2)
print(carro_removido)

#reverse inverte a ordem dos elementos na lista 

carros.reverse()
print(carros)


# para nao imprimir com os [] e as aspas da pra imprimir com for ou assim
# print(', '.join(lista_nomes)) 
 

numeros = [1, 2 , 3, 4, 5]
quadrado = [ num ** 2 for num in numeros if num%2 == 0]
print(quadrado)

# tupla / tuplas são imutáveis, não é possível alterar, excluir ou eliminar os elementos 

comidas = ("abacate", "feijão", "arroz", "abacate")

print(comidas[0])

# count, devolve o número de vezes que um elemento aparece na tupla

print(comidas.count("abacate"))

# index, fala onde ta 

#dicionários permitem a criação de chaves valor

pessoa = {"nome": "Gabriela", "idade": 18, "cachorro": "Pingo"}

print(pessoa["nome"]) #também da para obter o valor com get()

#keys retorna todas as chaves do dicionário

print(pessoa.keys())

#values retorna todos os valores do dicionário

print(pessoa.values())

#items retorna as chave valor

print(pessoa.items())

pessoa.update({"profissao": "engenheira de dados"})
print(pessoa)

# conjuntos / elementos únicos, mutáveis e não ordenados 

dispositivos = {"fone", "celular", "tablet"}

eletrodomesticos = set(["batedeira","airfryer"]) # da pra atribuir assim com set

#da pra fazer união, interseção e a diferença e a diferença simétrica


uniao = dispositivos | eletrodomesticos
print(uniao)

conjunto1 = {1,2,3}
conjunto2 ={3,4,5}
intersecao = conjunto1 & conjunto2 #elemento igual nos dois conjuntos
print(intersecao)

diferenca = conjunto1 - conjunto2 # imprime o que tem no 1 e não tem no 2 
print(diferenca)

diferenca_simetrica = conjunto1 ^ conjunto2 # imprime o que não tem nos dois conjuntos
print(diferenca_simetrica)


#add adiciona elementos no conjunto

peixes = {"barriguda", "caolho", "oncinha"}

peixes.add("fabio júnior")
print(peixes)

#remove, remove um item, se não existir gera um erro

peixes.remove("barriguda")

#discard remove um item mas se não existir não faz nada 

peixes.discard("barriguda")

#clear remove tudo

peixes.clear()

#funcoes

def oi():
    print("oi")


# Classifica a lista em ordem crescente.
sort(): 

# Ele retorna o tipo de classe de um objeto
type(lista)

#Adiciona um único elemento a uma lista.
append()

#Adiciona vários elementos a uma lista.
extend()

#: Retorna a primeira aparição do valor especificado.
index()

#Ele retorna um item da lista com o valor máximo.

max(list)

# Ele retorna um item da lista com o valor mínimo.
min(lista)

#Ele fornece o comprimento total da lista.
len(list)

#Converte uma tupla em uma lista.
list(seq)

# Ele compara os elementos de ambas as listas list1 e list2.
cmp(list1, list2)

# filtra a lista usando a função Python. 
filter(fun,list):


lista = [1, 2, 3, 4, 5]


ultimo_elemento = lista.pop()
print(ultimo_elemento)  
print(lista)  

elemento_removido = lista.pop(1)
print(elemento_removido)  
print(lista) 
#
"""
Remove o elemento no índice fornecido e retorna o valor removido. 
Se nenhum índice for fornecido, remove e retorna o último elemento da lista. 
Gera um IndexError se o índice estiver fora dos limites da lista. 
É útil quando você precisa acessar o valor do elemento removido. 

"""

remove():
    
"""
Remove a primeira ocorrência do valor especificado da lista.
Não retorna o valor removido.
Gera um ValueError se o valor não estiver na lista.
É útil quando você precisa remover uma ocorrência específica de um valor. 
"""

lista.remove(3)
print(lista) 

# remove() gera um ValueError se o valor não estiver na lista
try:
    lista.remove(9)
except ValueError:
    print("Valor não encontrado na lista")  



nomes = ["Alice", "Bob", "Charlie"]
idades = [25, 30, 28]
cidades = ["Lisboa", "Porto", "Braga"]

# Usando zip para combinar os elementos em tuplas
pessoas = zip(nomes, idades, cidades)

# Imprimindo as tuplas
for nome, idade, cidade in pessoas:
    print(f"{nome} tem {idade} anos e mora em {cidade}")
    
"""
A função zip() em Python combina vários iteráveis , como listas , tuplas , strings , dict etc., em um único iterador de tuplas. Cada tupla contém elementos dos iteráveis ​​de entrada que estão na mesma posição.

Vamos considerar um exemplo em que precisamos parear os nomes dos alunos com suas notas nos testes:
"""

nomes  = [ 'John' , 'Alice' , 'Bob' , 'Lucy' ]

pontuações  = [ 85 , 90 , 78 , 92 ]

res =  zip ( nomes , pontuações )

print(res)


[('João', 85), ('Alice', 90), ('Bob', 78), ('Lucy', 92)]


#zip() é usado para combinar as duas listas em um único iterável ' res '
#Cada elemento dos nomes é pareado com o elemento correspondente das pontuações
#list() converte o iterador de zip() em uma lista de tuplas, facilitando a visualização ou manipulação dos dados combinados.


lista1 = [1, 2, 3, 4]
lista2 = [3, 4, 5, 6]

# Convertendo em conjuntos
s1 = set(lista1)
s2 = set(lista2)

print(list(s1 | s2))  # União
print(list(s1 & s2))  # Interseção
print(list(s1 - s2))  # Diferença

tupla1 = (1, 2, 3)
tupla2 = (3, 4, 5)

s1 = set(tupla1)
s2 = set(tupla2)

print(tuple(s1 & s2))  # Interseção: (3,)



# set 

#Um conjunto mutável (pode adicionar/remover itens)
# Não ordenado
# Não aceita valores duplicados

# frozenset

#Um conjunto imutável
#Usado quando você precisa de um conjunto que não pode ser alterado
# Definição de dois conjuntos

conjunto_a = {1, 2, 3, 4, 5}
conjunto_b = {4, 5, 6, 7, 8}

# União: elementos que estão em A ou B (ou em ambos)
uniao = conjunto_a | conjunto_b

# Interseção: elementos que estão em A e B
intersecao = conjunto_a & conjunto_b

# Diferença: elementos que estão em A mas não estão em B
diferenca = conjunto_a - conjunto_b

# Exibição dos resultados
print("Conjunto A:", conjunto_a)

#treinando comits git hub

# Conjuntos de exemplo
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

# União - elementos em a OU b
uniao = a | b  # ou a.union(b)

# Interseção - elementos em a E b
intersecao = a & b  # ou a.intersection(b)

# Diferença - elementos em a mas NÃO em b
diferenca = a - b  # ou a.difference(b)

# Diferença simétrica - elementos em a OU b, mas NÃO nos dois
diferenca_simetrica = a ^ b  # ou a.symmetric_difference(b)

