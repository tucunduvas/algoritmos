alunos = []

def cadastrar_aluno():
    aluno = {
        'cpf': input("CPF do aluno: "),
        'nome': input("Nome: "),
        'endereço': {
            'rua': input("Rua: "),
            'bairro': input("Bairro: "),
            'cep': input("CEP: ")
        },
        'data_nasc': input("Data de nascimento (dd/mm): ")
    }
    alunos.append(aluno)
    
def buscar_aluno(cpf):
    return next((a for a in alunos if a['cpf'] == cpf), None)

