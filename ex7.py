nota = input("Digite a primeira nota: ")
nota2 = input("Digite a segunda nota: ")
nota3 = input("Digite a terceira nota: ")
nota4 = input("Digite a quarta nota: ")

media = (nota+nota2+nota3+nota4)/4
if media>6:
    print("Aluno aprovado")
else: 
    print("Aluno reprovado")