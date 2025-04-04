from random import randint
from time import sleep

jogadores = dict()
ranking = list()
for i in range(1, 5):
    jogadores[f'jogador {i}'] = randint(1, 6)
print('Valores sorteados:')
for k, v in jogadores.items():
    print(f'  O {k} tirou {v} no dado.')
    sleep(1)
ranking = sorted(jogadores.items(), key=lambda x: x[1], reverse=True)
print('Ranking dos jogadores:')
for i, v in enumerate(ranking):
    print(f'  {i+1}º lugar: {v[0]} com {v[1]}.')
    sleep(1)
print('-=' * 30)
print('Fim do programa.')