dic = {'nome': ['maria','gabi']}
print(dic['nome'][0])

dic3 ={('nome','idade'):('gabi',18)}

lista1 = [
    {'nome':'gabi', 'endereço': ('rua', 'cep')},
    {'nome':'livia', 'endereço': ('bairro', 'cidade')},
    {'nome':['livia', 'matheus'], 'endereço': ('bairro', 'cidade')}
]

lista1 = [
    {'nome': 'gabi', 'endereço': ('rua', 'cep')},
    {'nome': 'livia', 'endereço': ('bairro', 'cidade')},
    {'nome': ['livia', 'matheus'], 'endereço': ('bairro', 'cidade')}
]

for i, item in enumerate(lista1):
    print(f"--- Pessoa {i+1} ---")

    nome = item['nome']
    endereco = item['endereço']

    if isinstance(nome, list):
        print("Nomes:")
        for n in nome:
            print(f" - {n}")
    else:
        print(f"Nome: {nome}")

    print("Endereço:")
    print(f" - {endereco[0]}")
    print(f" - {endereco[1]}")
