"""

Exercício 1: Gerenciamento de Produtos com Dicionários e Listas
Você trabalha em uma loja e precisa gerenciar o estoque de produtos. Cada produto tem um ID, nome, preço e quantidade em estoque.
Crie uma lista de dicionários, onde cada dicionário representa um produto. Inclua pelo menos 3 produtos.
Escreva uma função que receba a lista de produtos e um ID de produto como argumento.
A função deve retornar o dicionário completo do produto correspondente ao ID. Se o produto não for encontrado, retorne None.
Crie uma função que receba a lista de produtos, um ID de produto e uma nova_quantidade. 
A função deve atualizar a quantidade do produto com o ID fornecido. Se o produto não for encontrado, imprima uma mensagem de erro.


"""

produtos = [
    {'id': 12, 'nome': 'bala', 'preço': 15.00, 'qntd': 5},
    {'id': 13, 'nome': 'pirulito', 'preço': 25.00, 'qntd': 37},
    {'id': 14, 'nome': 'chiclete', 'preço': 10.00, 'qntd': 3}
]

def funcao(lista, id):
    for p in lista:
        if p['id'] == id:
            print(p)
        else:
            None

def lista(lista, id, nova_qntd):
    for p in lista:
        if p['id'] == id:
            p['qntd'] = nova_qntd
            return p
        else:
            print("Produto não encontrado")


print(funcao(produtos, 13))
print(lista(produtos,12,67))