import datetime
pessoas = []
for a in range (1, 8):
    pessoas.append(int(input(f"Informe a data de nascimento da {a}ª pessoa: ")))
ano_atual = datetime.datetime.today().year
maioridade = 0
minoridade = 0
for i in range(len(pessoas)):
    if ano_atual - pessoas[i] >= 18:
        maioridade += 1
    else:
        minoridade += 1
print(f"Segundo os dados informados:\nMaior de 18 anos: {maioridade}\nMenor de 18 anos: {minoridade}")