altura = float(input("Digite a altura: "))
sexo = input("Informe o sexo, digite feminino ou masculino: ").lower()

if sexo == "masculino":
    peso_ideal = (72.7*altura)-58 
    print("O peso ideal é: ", peso_ideal)
elif sexo == "feminino":
    peso_ideal = (62.1*altura)-44.7
    print("O peso ideal é: ", peso_ideal)
else:
    print("Não identificado")

