nota = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
nota4 = float(input("Digite a quarta nota: "))

media = (nota+nota2+nota3+nota4)/4
if media>=6:
    print(f"Aluno aprovado, com média {media}")
elif 4<=media<6:
    print(f"O aluno está na recuperação, com média {media}")
else: 
    print(f"Está reprovado, com média {media}")
