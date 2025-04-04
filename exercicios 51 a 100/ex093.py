jogador = dict()

jogador['nome'] = str(input('Nome do jogador: '))
partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
gols = list()
total = 0
for i in range(0, partidas):
    gols.append(int(input(f'  Quantos gols na partida {i+1}? ')))
    total += gols[i]
jogador['gols'] = gols
jogador['total'] = total
print('-=' * 30)
print(f"O jogador {jogador['nome']} jogou {partidas} partidas.")
for i, v in enumerate(jogador['gols']):
    print(f'  => Na partida {i+1}, fez {v} gols.')
print(f"Foi um total de {jogador['total']} gols.")
print('-=' * 30)
print('Fim do programa.')
