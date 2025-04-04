jogador = dict()
time = list()

while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do jogador: '))
    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    gols = list()
    total = 0
    for i in range(0, partidas):
        gols.append(int(input(f'  Quantos gols na partida {i+1}? ')))
        total += gols[i]
    jogador['gols'] = gols
    jogador['total'] = total
    time.append(jogador.copy())
    print('-=' * 30)
    print(f"O jogador {jogador['nome']} jogou {partidas} partidas.")
    for i, v in enumerate(jogador['gols']):
        print(f'  => Na partida {i+1}, fez {v} gols.')
    print(f"Foi um total de {jogador['total']} gols.")
    print('-=' * 30)
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp in 'N':
        break
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-' * 40)
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-' * 40)
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! Não existe jogador com código {busca}!')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}:')
        for i, g in enumerate(time[busca]['gols']):
            print(f'  No jogo {i+1} fez {g} gols.')
    print('-' * 40)
print('<< VOLTE SEMPRE >>')
print('-=' * 30)
print('Fim do programa.')