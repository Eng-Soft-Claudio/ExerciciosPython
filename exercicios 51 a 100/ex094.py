from datetime import datetime

grupo = list()
pessoa = dict()
total = 0

while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    pessoa['sexo'] = str(input('Sexo: '))
    pessoa['idade'] = datetime.today().year - int(input('Ano de nascimento: '))
    total += pessoa['idade']
    grupo.append(pessoa.copy())
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp in 'N':
        break
print('-=' * 30)
print(f'A) Ao todo temos {len(grupo)} pessoas cadastradas.')
print(f'B) A média de idade é de {total / len(grupo):.2f} anos.')
print(f'C) As mulheres cadastradas foram: ', end='')
for p in grupo:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]} ', end='')
print()
print(f'D) Lista das pessoas que estão acima da média:')
for p in grupo:
    if p['idade'] > total / len(grupo):
        print('  ', end='')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('<< ENCERRADO >>')
print('-=' * 30)
print('Fim do programa.')