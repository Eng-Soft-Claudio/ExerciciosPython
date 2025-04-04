from random import randint
from time import sleep
lista = []
print("-" * 40)
print(f'{"JOGOS PARA MEGA SENA":^40}')
print("-" * 40)

qtde_jogos = int(input("Quantos jogos deseja? "))
print(f"-=-=-=-=-= SORTEANDO  {qtde_jogos} JOGOS =-=-=-=-=-")

for jogo in range (0, qtde_jogos):
    for numero in range(0, 6):
        palpite = randint(1, 61)
        if palpite not in lista:
            lista.append(palpite)
    sleep(0.5)
    print(f"JOGO {jogo+1}: {lista}")
    lista.clear()
print("-=-=-=-=-=-=-= BOA SORTE! =-=-=-=-=-=-=-")
