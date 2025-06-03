
professores = []

def cadastrar_professor():
    professor = {
        'cpf': input("CPF do professor: "),
        'nome': input("Nome: "),
        'endereço': {
            'rua': input("Rua: "),
            'bairro': input("Bairro: "),
            'cep': input("CEP: ")
        },
        'data_nasc': input("Data de nascimento (dd/mm): ")
    }
    professores.append(professor)
