nome = input("Digite o nome: ")
salario = float(input("Digite o salário bruto: "))

inss = salario*0.08
salario_liquido = salario - inss

print("O nome do funcionário é", nome)
print("O valor do salário liquído é: ", salario_liquido)
