"""


faça exercícios de manipulação de lista com dicionário e tupla em python, args, kwargs, map, filter, reduce




Vamos explorar alguns exercícios de manipulação de dados em Python, combinando listas, dicionários, tuplas e utilizando *args, **kwargs, map, filter e reduce.

Exercícios de Manipulação de Dados em Python
Exercício 1: Gerenciamento de Produtos com Dicionários e Listas
Você trabalha em uma loja e precisa gerenciar o estoque de produtos. Cada produto tem um ID, nome, preço e quantidade em estoque.

Crie uma lista de dicionários, onde cada dicionário representa um produto. Inclua pelo menos 3 produtos.

Escreva uma função que receba a lista de produtos e um ID de produto como argumento. A função deve retornar o dicionário completo do produto correspondente ao ID. Se o produto não for encontrado, retorne None.

Crie uma função que receba a lista de produtos, um ID de produto e uma nova_quantidade. A função deve atualizar a quantidade do produto com o ID fornecido. Se o produto não for encontrado, imprima uma mensagem de erro.

Exemplo de dados:

Python

produtos = [
    {"ID": "001", "nome": "Teclado Mecânico", "preço": 150.00, "quantidade": 20},
    {"ID": "002", "nome": "Mouse Gamer", "preço": 80.00, "quantidade": 35},
    {"ID": "003", "nome": "Monitor Ultrawide", "preço": 1200.00, "quantidade": 10}
]
Exercício 2: Análise de Dados de Alunos com Tuplas e map/filter
Você tem uma lista de tuplas, onde cada tupla representa um aluno com seu nome, nota_matematica, nota_portugues e nota_ciencia.

Crie uma lista de tuplas com pelo menos 4 alunos.

Use map para criar uma nova lista contendo apenas a média das notas de cada aluno. A média deve ser arredondada para duas casas decimais.

Use filter para criar uma nova lista contendo apenas os nomes dos alunos que foram aprovados. Considere que um aluno é aprovado se a média de suas notas for maior ou igual a 7.0.

Exemplo de dados:

Python

alunos = [
    ("Alice", 8.5, 7.0, 9.0),
    ("Bruno", 6.0, 6.5, 7.0),
    ("Carla", 9.0, 8.0, 8.5),
    ("Daniel", 5.5, 4.0, 6.0)
]
Exercício 3: Operações Flexíveis com *args e **kwargs
Crie uma função chamada processar_operacao que aceite um número variável de argumentos posicionais (*args) e argumentos nomeados (**kwargs).

Se kwargs contiver a chave 'operacao' com o valor 'soma', a função deve retornar a soma de todos os args.

Se kwargs contiver a chave 'operacao' com o valor 'multiplicacao', a função deve retornar o produto de todos os args.

Se kwargs contiver a chave 'operacao' com o valor 'concatenar', a função deve concatenar todos os args (assumindo que são strings) e retornar o resultado.

Para qualquer outra operação, a função deve imprimir uma mensagem de "Operação inválida".

Exemplo de chamadas:

Python

# Exemplo de soma
processar_operacao(1, 2, 3, 4, operacao='soma') # Deve retornar 10

# Exemplo de multiplicação
processar_operacao(2, 3, 4, operacao='multiplicacao') # Deve retornar 24

# Exemplo de concatenação
processar_operacao("Olá", " ", "Mundo", "!", operacao='concatenar') # Deve retornar "Olá Mundo!"

# Exemplo de operação inválida
processar_operacao(10, 20, operacao='divisao')
Exercício 4: Agregação com reduce
Você tem uma lista de números inteiros.

Use reduce (da biblioteca functools) para encontrar o maior número na lista.

Use reduce para calcular o produto de todos os números na lista.

Exemplo de dados:

Python

from functools import reduce

numeros = [5, 12, 3, 8, 20, 1]
Sinta-se à vontade para resolver os exercícios e, se tiver dúvidas ou quiser comparar suas soluções, pode perguntar!

coloque em um pdf



Não consigo gerar um arquivo PDF diretamente aqui. No entanto, posso te ajudar de outras formas:

Fornecer o conteúdo em texto: Posso te entregar o conteúdo dos exercícios em formato de texto, que você pode copiar e colar em um editor de texto (como Word, Google Docs, Bloco de Notas) e depois exportar ou imprimir como PDF.

Sugestões de ferramentas: Posso te dar algumas sugestões de ferramentas online ou programas que você pode usar para converter texto em PDF.

Qual dessas opções seria mais útil para você?


coloque em texto



Com certeza! Abaixo estão os exercícios em formato de texto, que você pode copiar e colar onde precisar.

Exercícios de Manipulação de Dados em Python
Exercício 1: Gerenciamento de Produtos com Dicionários e Listas
Você trabalha em uma loja e precisa gerenciar o estoque de produtos. Cada produto tem um ID, nome, preço e quantidade em estoque.

Crie uma lista de dicionários, onde cada dicionário representa um produto. Inclua pelo menos 3 produtos.

Escreva uma função que receba a lista de produtos e um ID de produto como argumento. A função deve retornar o dicionário completo do produto correspondente ao ID. Se o produto não for encontrado, retorne None.

Crie uma função que receba a lista de produtos, um ID de produto e uma nova_quantidade. A função deve atualizar a quantidade do produto com o ID fornecido. Se o produto não for encontrado, imprima uma mensagem de erro.

Exemplo de dados:

Python

produtos = [
    {"ID": "001", "nome": "Teclado Mecânico", "preço": 150.00, "quantidade": 20},
    {"ID": "002", "nome": "Mouse Gamer", "preço": 80.00, "quantidade": 35},
    {"ID": "003", "nome": "Monitor Ultrawide", "preço": 1200.00, "quantidade": 10}
]
Exercício 2: Análise de Dados de Alunos com Tuplas e map/filter
Você tem uma lista de tuplas, onde cada tupla representa um aluno com seu nome, nota_matematica, nota_portugues e nota_ciencia.

Crie uma lista de tuplas com pelo menos 4 alunos.

Use map para criar uma nova lista contendo apenas a média das notas de cada aluno. A média deve ser arredondada para duas casas decimais.

Use filter para criar uma nova lista contendo apenas os nomes dos alunos que foram aprovados. Considere que um aluno é aprovado se a média de suas notas for maior ou igual a 7.0.

Exemplo de dados:

Python

alunos = [
    ("Alice", 8.5, 7.0, 9.0),
    ("Bruno", 6.0, 6.5, 7.0),
    ("Carla", 9.0, 8.0, 8.5),
    ("Daniel", 5.5, 4.0, 6.0)
]
Exercício 3: Operações Flexíveis com *args e **kwargs
Crie uma função chamada processar_operacao que aceite um número variável de argumentos posicionais (*args) e argumentos nomeados (**kwargs).

Se kwargs contiver a chave 'operacao' com o valor 'soma', a função deve retornar a soma de todos os args.

Se kwargs contiver a chave 'operacao' com o valor 'multiplicacao', a função deve retornar o produto de todos os args.

Se kwargs contiver a chave 'operacao' com o valor 'concatenar', a função deve concatenar todos os args (assumindo que são strings) e retornar o resultado.

Para qualquer outra operação, a função deve imprimir uma mensagem de "Operação inválida".

Exemplo de chamadas:

Python

# Exemplo de soma
processar_operacao(1, 2, 3, 4, operacao='soma') # Deve retornar 10

# Exemplo de multiplicação
processar_operacao(2, 3, 4, operacao='multiplicacao') # Deve retornar 24

# Exemplo de concatenação
processar_operacao("Olá", " ", "Mundo", "!", operacao='concatenar') # Deve retornar "Olá Mundo!"

# Exemplo de operação inválida
processar_operacao(10, 20, operacao='divisao')
Exercício 4: Agregação com reduce
Você tem uma lista de números inteiros.

Use reduce (da biblioteca functools) para encontrar o maior número na lista.

Use reduce para calcular o produto de todos os números na lista.

Exemplo de dados:

Python

from functools import reduce

numeros = [5, 12, 3, 8, 20, 1]
"""