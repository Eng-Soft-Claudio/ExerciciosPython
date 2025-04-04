import random
print("="*50)
alunos = []
for a in range (4):
    alunos.append(input("Informe o nome de um aluno: "))
print("="*50)
print(f"O aluno sorteado foi: {random.choice(alunos)}")
print("="*50)