
# Exercício 3: Operações Flexíveis com *args e **kwargs
# Crie uma função chamada processar_operacao que aceite um número variável de argumentos posicionais (*args) e argumentos nomeados (**kwargs).

# Se kwargs contiver a chave 'operacao' com o valor 'soma', a função deve retornar a soma de todos os args.

# Se kwargs contiver a chave 'operacao' com o valor 'multiplicacao', a função deve retornar o produto de todos os args.

# Se kwargs contiver a chave 'operacao' com o valor 'concatenar', a função deve concatenar todos os args (assumindo que são strings) e retornar o resultado.

# Para qualquer outra operação, a função deve imprimir uma mensagem de "Operação inválida".



def calculadora(*args, **kwargs):
    resultado = 1
    if kwargs['operacao'] == 'soma':
        print(sum(args))
    elif kwargs['operacao'] == 'mult':
        for num in args:
            resultado *= num
        print(resultado)
    elif kwargs['operacao'] == 'concatenar':
        if isinstance(args, str):
            print(''.join(args))
        else:
            print(''.join(str(args)))
    else:
        print("Operação inválida")
    if kwargs['detalhes'] == True:
        print(args, kwargs)
        
calculadora(1,2,3, operacao = 'mult', detalhes = True)
