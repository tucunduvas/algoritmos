def relatorio():
    print("Relatório ainda não implementado.")
    input("Pressione ENTER para voltar.")

def sair():
    print("Saindo do sistema.")
    exit()

opcoes = {
    1: menu_cadastro,
    2: matricula,
    3: listar,
    4: relatorio,
    0: sair
}

# Executar a função correspondente
func = opcoes.get(op, lambda: print("Opção inválida."))
func()
