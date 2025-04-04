import random
print("=" * 50)
alunos = []
for a in range(4):
    alunos.append(input("Informe o nome do aluno: "))
print("=" * 50)
random.shuffle(alunos)
print(f"Ordem de apresentação dos alunos:")
for a in range(4):
    print(alunos[a])