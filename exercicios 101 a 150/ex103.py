def placar(jogador = 'desconhecido', gols = 0):
    print(f'O jogador {jogador} fez {gols} gol(s) no campeonato.')
jogador = str(input('Nome do jogador: '))
gols = str(input('Número de gols: '))
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
if jogador.strip() == '':
    placar(gols = gols)
else:
    placar(jogador, gols)
