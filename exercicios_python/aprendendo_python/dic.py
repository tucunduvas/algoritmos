
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