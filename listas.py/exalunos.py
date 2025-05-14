import random



oi = random.randrange(5)


x = random.randint(0,100)
notas = list()

for x in range(4):
    notas.append(x)

alunos = [{"nome": f"aluno{i+1}"} for i in range(50)]
alunos = [f"Aluno{i+1}" for i in range(50)]
for aluno in alunos:
    
