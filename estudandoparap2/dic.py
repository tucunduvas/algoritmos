# Criação de dicionário
d = {'nome': 'João', 'idade': 30, 'cidade': 'São Paulo'}

# Acesso a valores
print(d['nome'])  # João

# Adição de nova chave
d['profissão'] = 'Engenheiro'

# Atualização de valor
d['idade'] = 31

# Remoção de item com del
del d['cidade']

# Remoção com pop
profissao = d.pop('profissão')  # Retorna o valor e remove a chave

# Limpar dicionário
d.clear()

# Copiar dicionário
d1 = {'a': 1, 'b': 2}
d2 = d1.copy()

# Obter todas as chaves
print(d1.keys())

# Obter todos os valores
print(d1.values())

# Obter todos os itens (pares chave-valor)
print(d1.items())

# Verificar se chave existe
print('a' in d1)  # True

# Criar dicionário com fromkeys
chaves = ['nome', 'idade', 'cidade']
d3 = dict.fromkeys(chaves, None)

# Acessar valor com get (evita erro se chave não existe)
print(d1.get('c'))  # None

# Atualizar dicionário com outro
d1.update({'c': 3, 'a': 100})

# Iterar por chaves
for chave in d1:
    print(chave, d1[chave])

# Iterar por chave e valor
for chave, valor in d1.items():
    print(chave, valor)

# Compreensão de dicionários (dict comprehension)
quadrados = {x: x**2 for x in range(5)}  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
