animais = ('tamanduá', 'cobra', 'elefante', 'macaco', 'leão', 'peixe', 'cachorro', 'gato', 'rato', 'coelho')

for i, valor in enumerate(animais):
    if i<4:
        print(f"Quatro primeiros nomes: {valor}")
    if i>7:
        print(f"Dois últimos nomes: {valor}")
    if valor=='gato':
        print(f"Gato está na posição {i}")
        
quatro_primeiros = [x for i,x in enumerate(animais) if i<4]
dois_ultimos = [x for i,x in enumerate(animais) if i>7]
gato = [i for i,x in enumerate(animais) if x=='gato']

print(sorted(animais))
print(f"Quatro primeiros nomes: {quatro_primeiros}")
print(f"Dois últimos nomes: {dois_ultimos}")
print(f"Gato está na posição {gato}")
