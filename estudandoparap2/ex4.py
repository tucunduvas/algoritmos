# Exercício 6 - Contar frequência de caracteres (ignorando espaços)
texto6 = "banana split"
# Saída esperada: {'b': 1, 'a': 3, 'n': 2, 's': 1, 'p': 1, 'l': 1, 'i': 1, 't': 1}
texto6 = texto6.replace(" ", "")
palavra = {}
for i in texto6:
    if isinstance(i, str):
        palavra[i] = texto6.count(i)
    
print(palavra)