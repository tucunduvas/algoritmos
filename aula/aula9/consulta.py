from aluno import alunos
from professor import professores
from turma import turmas

def listar():
    print("** CONSULTA **")
    print("1 - Alunos")
    print("2 - Professores")
    print("3 - Turmas")
    print("0 - Voltar")
    op = int(input("Escolha: "))
    
    if op == 1:
        print("Alunos:")
        for a in alunos:
            print(a)
    elif op == 2:
        print("Professores:")
        for p in professores:
            print(p)
    elif op == 3:
        print("Turmas:")
        for t in turmas:
            print(f"Turma: {t['nome']}")
            for a in t['alunos']:
                print(f"  - {a['nome']}")
    input("Pressione ENTER para continuar...")
