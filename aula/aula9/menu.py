from util import limpar_tela
from aluno import cadastrar_aluno, buscar_aluno
from professor import cadastrar_professor
from consulta import listar
from turma import matricular_aluno

def menu_principal():
    limpar_tela()
    print("************ MENU *************")
    print("1 - cadastrar ")
    print("2 - matricular ")
    print("3 - consultar ")
    print("4 - relatório ")
    print("0 - sair ")
    op = ler_opcao(4)
    
    
    if op == 1:
        menu_cadastro()
    elif op == 2:
        matricula()
    elif op == 3:
        listar()
    elif op == 4:
        print("Relatório ainda não implementado.")
        input("Pressione ENTER para voltar.")
    elif op == 0:
        print("Saindo do sistema.")
        exit()

def menu_cadastro():
    limpar_tela()
    print("** CADASTRAR **")
    print("1 - Aluno")
    print("2 - Professor")
    print("3 - Voltar")
    op = ler_opcao(3)
    
    if op == 1:
        cadastrar_aluno()
    elif op == 2:
        cadastrar_professor()

def matricula():
    limpar_tela()
    print("** MATRÍCULA **")
    cpf = input("Digite o CPF do aluno: ")
    aluno = buscar_aluno(cpf)
    if aluno:
        turma = input("Nome da turma: ")
        matricular_aluno(aluno, turma)
        print(f"{aluno['nome']} foi matriculado na turma {turma}.")
    else:
        print("Aluno não encontrado.")
    input("Pressione ENTER para continuar...")

def ler_opcao(lim_sup):
    try:
        op = int(input("Escolha uma opção: "))
        if 0 <= op <= lim_sup:
            return op
    except ValueError:
        pass
    print("Opção inválida.")
    input("Pressione ENTER para continuar...")
    return -1


    
