import random

alunos = list()

for i in range(50):
    nome = f"Aluno{i+1}"
    notas = [random.randint(0, 100) for i in range(4)]
    media = sum(notas) / 4
    alunos.append({
        "nome": nome,
        "notas": notas,
        "media": media
    })

aprovados = list()
reprovados = list()

for aluno in alunos:
    if aluno["media"] >= 60:
        aprovados.append(aluno)
    else:
        reprovados.append(aluno)

qntd_aprovados = len(aprovados)
qntd_reprovados = len(reprovados)
qntd_total = len(alunos)

porcentagem_aprovados = (qntd_aprovados/ qntd_total) * 100
porcentagem_reprovados = (qntd_reprovados / qntd_total) * 100

print(f"Porcentagem de alunos aprovados: {porcentagem_aprovados}")

print(f"Porcentagem de alunos reprovados: {porcentagem_reprovados}")

ordem_crescente = notas.sort()




