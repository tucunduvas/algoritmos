palavra = 'ovo'

invertida = palavra[::-1]
invertida2 = ''.join(reversed(palavra))

def palindromos(lista):
    palindromos_list = list()
    for i in lista:
        if i == i[::-1]:
            palindromos_list.append(i)
    return palindromos_list

print(palindromos(['ovo', 'radar', 'sim', 'nao']))