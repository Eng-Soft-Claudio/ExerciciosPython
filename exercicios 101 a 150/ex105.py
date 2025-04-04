# Função
def notas(*notas, situacao=False):
    """
    Calcula estatísticas sobre as notas de um aluno e, opcionalmente, sua situação.

    :para as notas: Notas do aluno (quantidade variável).
    :para a situacao: (opcional) Indica se a situação do aluno deve ser incluída.
    :return: Um dicionário com total de notas, maior, menor, média e, se solicitado, a situação.
    """
    aluno = dict()
    aluno['total'] = len(notas)
    aluno['maior'] = max(notas)
    aluno['menor'] = min(notas)
    aluno['media'] = sum(notas) / len(notas)
    if situacao:
        if aluno['media'] >= 7:
            aluno['situacao'] = 'Aprovado'
        elif aluno['media'] >= 5:
            aluno['situacao'] = 'Recuperação'
        else:
            aluno['situacao'] = 'Reprovado'
    return aluno

# Bloco principal
qtde_notas = int(input('Quantas notas você quer informar? '))
lista_notas = list()

for n in range(qtde_notas):
    while True:
        try:
            nota = float(input(f'Nota {n+1}: '))
            lista_notas.append(nota)
            break
        except ValueError:
            print("Por favor, insira um número válido.")

while True:
    situacao = input('Deseja informar a situação do aluno? [S/N] ').strip().upper()
    if situacao in ['S', 'N']:
        situacao = True if situacao == 'S' else False
        break
    else:
        print("Resposta inválida! Digite 'S' para Sim ou 'N' para Não.")

# Chamada da função com desempacotamento da lista
print(notas(*lista_notas, situacao=situacao))