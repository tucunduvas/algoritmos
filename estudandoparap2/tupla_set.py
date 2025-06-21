# Criar tupla
tupla = (1, 2, 3, 4)

# Acessar elementos
print(tupla[0])  # 1
print(tupla[-1])  # 4

# Fatiamento
print(tupla[1:3])  # (2, 3)

# Contar quantas vezes um elemento aparece
print(tupla.count(2))  # 1

# Obter índice de um elemento
print(tupla.index(3))  # 2

# Iterar sobre tupla
for item in tupla:
    print(item)

# Verificar se elemento está na tupla
print(2 in tupla)  # True

# Tupla com um único elemento (atenção à vírgula)
t1 = (5,)  # isso é uma tupla
t2 = (5)   # isso é um int

# Converter lista para tupla
lista = [1, 2, 3]
tupla_convertida = tuple(lista)

# Desempacotar tupla
a, b, c, d = tupla
print(a, b, c, d)

tupla = (10, 20, 30, 40)

a, b, c, d = tupla

a = 10
b = 20
c = 30
d = 40
