def oi():
    print("oi")

oi()

def adicao(x,y):
    soma = x+y
    print(soma)

adicao(15,5)



def subtracao(a,b):
    return a-b 

operacao = subtracao(7,4)
print(operacao)

#funcoes anonimas ou lambda

cubo = lambda i: i**3
print(cubo(2))

# versao normal com  return 

def cubo(x):
    return x**3

Cubo = cubo(3)
print(Cubo)

def variavel1():
    variavel_local = 10
    print(variavel_local)

variavel_global = 20

def variavel2():
    print(variavel_global)

#try except

try:
    divisao = 10/0
    print(divisao)
except ZeroDivisionError:
    print("Erro: Divisão por 0")


try:
    # Código que pode gerar uma exceção
    arquivo = open("arquivo.txt", "r")
    # Realizar operações com o arquivo
except FileNotFoundError:
    print("Erro: Arquivo não encontrado")
finally:
    arquivo.close()  # Fechar o arquivo sempre, mesmo se ocorrer uma exceção

#criar excecoes personalizadas

def funcao():
    
    if condicao:
        raise Exception("descrição de erro")
    
try:
    funcao()
except Exception as e:
    print(f"Erro: {str(e)}")
    

