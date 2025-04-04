def contador(inicio, fim, passo):
    for valor in range(1, 11, 1):
        print(f'{valor} ', end='')
    print()
    for valor in range(10, -2, -2):
        print(f'{valor} ', end='')
    print()
    for valor in range(inicio, fim + passo, passo):
        print(f'{valor} ', end='')
    print('Fim do programa.')
    return

inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(inicio, fim, passo)
