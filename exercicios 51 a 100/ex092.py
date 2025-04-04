from datetime import datetime

trabalhador = dict()
trabalhador['nome'] = str(input('Nome: '))
trabalhador['idade'] = datetime.today().year - int(input('Ano de nascimento: '))
trabalhador['ctps'] = int(input('Carteira de trabalho (0 não tem): '))

if trabalhador['ctps'] != 0:
    trabalhador['ano_contrato'] = int(input('Ano de contratação: '))
    trabalhador['salario'] = float(input('Salário: R$'))
    trabalhador['aposentadoria'] = trabalhador['idade'] + ((trabalhador['ano_contrato'] + 35) - datetime.today().year)

print('-=' * 30)
for k, v in trabalhador.items():
    print(f'  - {k} tem o valor {v}')
print('-=' * 30)
print('Fim do programa.')