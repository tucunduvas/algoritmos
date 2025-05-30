from util import limpar_tela
from  aluno import  cadastrar_aluno
from professor import cadastrar_professor
def menu_principal():
    limpar_tela()
    print("************ MENU *************")
    print("1 - cadastrar ")
    print("2 - matricular ")
    print("3 - consultar ")
    print("4 - relatório ")
    print("0 - sair ")
    op = ler_opcao(4)
    
    #melhorar 
    if op == 1:
        menu_cadastro()
        
def menu_cadastro():
    limpar_tela()
    print("**cadastrar**")
    print("** aluno **")
    print("**professor**")
    print("**voltar**")
    op = ler_opcao(3)
    
    if op == 1:
        cadastrar_aluno()
    elif op==2:
        cadastrar_professor()



def matricula():
    print("** matricula**")
    print("** aluno**")
    print("**voltar**")
    op = ler_opcao(1)
    
def ler_opcao(lim_sup):
    op = input("escolha uma opção: ")
    if  op>= 0 and op<=lim_sup:
        return op
    print("nao existe essa opcao")
    return -1 
    
