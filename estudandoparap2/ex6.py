# Exercício 7 - Anagramas (agrupar palavras com mesmas letras)
palavras7 = ['amor', 'roma', 'carro', 'arco', 'roca']
# Saída esperada: {'amor': ['amor', 'roma'], 'carro': ['carro'], 'arco': ['arco', 'roca']}
dic = {}
for i in palavras7:
    dic[i] = list(x for x in palavras7 if sorted(x) == sorted(i))

print(dic)