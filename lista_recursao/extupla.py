"""

Exercício 2: Análise de Dados de Alunos com Tuplas e map/filter
Você tem uma lista de tuplas, onde cada tupla representa um aluno com seu nome, nota_matematica, nota_portugues e nota_ciencia.

Crie uma lista de tuplas com pelo menos 4 alunos.

Use map para criar uma nova lista contendo apenas a média das notas de cada aluno.
A média deve ser arredondada para duas casas decimais.

Use filter para criar uma nova lista contendo apenas os nomes dos alunos que foram aprovados.
Considere que um aluno é aprovado se a média de suas notas for maior ou igual a 7.0.

"""


lista = [
    ('Ana',10, 9, 8), 
    ('Marcio',6, 5, 4), 
    ('Beto',10, 9, 8), 
    ('Gabi',10, 9, 8), 
]

tupla_comprensao = tuple(x for x in lista if isinstance(x, int))
media = list(map(lambda x: sum(x)/len(x), tupla_comprensao ))


print(tupla_comprensao)