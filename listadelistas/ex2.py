"""
    Exercıcios Faceis
1. Crie uma lista com 5 numeros inteiros. Imprima o tamanho da lista usando len.
2. Solicite ao usuario 5 nomes e armazene em uma lista. Depois, imprima cada nome
em uma linha.
3. Crie uma lista vazia e adicione 3 elementos usando append. Imprima a lista
"""
nomes = list()
for _ in range(5):
    nome = input("Digite 5 nomes: ")
    nomes.append(nome)
    
print(nomes)