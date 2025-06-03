"""
Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
A) Apenas os 5 primeiros colocados.
B) Os últimos 4 colocados da tabela.
C) Uma lista com os times em ordem alfabética.
D) Em que posição na tabela está o time da mirassol.
"""

times_brasileirao = (
    "Flamengo",
    "Cruzeiro",
    "Red Bull Bragantino",
    "Palmeiras",
    "Fluminense",
    "Bahia",
    "Mirassol",
    "Atlético-MG",
    "Botafogo",
    "Ceará",
    "Corinthians",
    "Grêmio",
    "São Paulo",
    "Internacional",
    "Vasco",
    "Vitória",
    "Fortaleza",
    "Santos",
    "Sport",
    "Juventude"
)

print("CINCO PRIMEIROS COLOCADOS:")
for i in range(5):
    print(times_brasileirao[i])

print("QUATRO ÚLTIMOS COLOCADOS:")
for j in range(1,5):
    print(times_brasileirao[-j])

print("EM ORDEM ALFABÉTICA:")
for i in sorted(times_brasileirao):
    print(i)
    
print(f"O time Mirassol está na posição {times_brasileirao.index('Mirassol')}")