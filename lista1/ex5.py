nome = input("Digite o nome: ")
funcoes = int(input("Digite a quantidade de funcoes: "))
valor = int(input("Digite o valor da função: "))

salario = valor*funcoes
"""
    n=1
while n<=funcoes:
    salario = float(input("Digite o valor da função: "))
    salario
    n=n+1
    
print(salario)
    """


inss = salario*0.08
salario_bruto = salario-inss

print(f"O funcionário se chama: {nome} seu salário liquído é R${salario}  e o salário bruto é R${salario_bruto}")