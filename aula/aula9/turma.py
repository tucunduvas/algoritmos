# turma.py
turmas = []

def matricular_aluno(aluno, turma_nome):
    turma = next((t for t in turmas if t['nome'] == turma_nome), None)
    if not turma:
        turma = {'nome': turma_nome, 'alunos': []}
        turmas.append(turma)
    turma['alunos'].append(aluno)
