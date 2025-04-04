ficha = []
print("=" * 22)

while True:

    nome = str(input("Nome do aluno: ")).capitalize().strip()
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))

    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    
    loop = str(input("Deseja continuar [S/N]: ")).upper().strip()[0]
    if loop == "N":
        break

    print("=" * 22)

print("=" * 22)
print(f"{'Nº.':<7}{'NOME':<10}{'MÉDIA':>5}")

for indice, aluno in enumerate(ficha):
    print(f"{indice+1:<7}{aluno[0]:<10}{aluno[2]:>5.1f}")
print("=" * 22)