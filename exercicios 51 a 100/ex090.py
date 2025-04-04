alunos = dict()
alunos['nome'] = str(input('Nome: '))
alunos['media'] = float(input(f'Média de {alunos["nome"]}: '))
if alunos['media'] >= 7:
    situacao = 'Aprovado'
elif 5 <= alunos['media'] < 7:
    situacao = 'Recuperação'
else:
    situacao = 'Reprovado'
alunos['situacao'] = situacao
print('-=' * 30)
for k, v in alunos.items():
    print(f'  - {k} é igual a {v}')
print('-=' *30)
