frutas = ["pera", "maça", "banana"]

for fruta in frutas:
    print(fruta)

numeros = [1, 2 ,3]

"""
for numero in numeros:
    resultado = array_sum()
"""

contador= 0 

while contador<=5:
    print(contador)
    contador+=1

resultado = 0 
Contador = 0 

while Contador<5:
    resultado = resultado + Contador
    Contador+=1
    print(resultado)


contador = 0


while True:

    print(contador)
    contador += 1


    if contador == 5:
        break

for i in range(10):

    if i % 2 == 0: #se o i for par o continue não vai executar o print, por isso só os números impares são impressos porque 
        continue   # se o número for ímpar não vai cair no if e o continue ta dentro do if 
    print(i)

for i in range(20):
    pass 

#listas 

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

