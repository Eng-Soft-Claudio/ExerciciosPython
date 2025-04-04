def numero_maior(*num):
    print(f'Os valores passados foram {num}')
    print(f'O maior valor passado foi {max(num)}')
    print('Fim do programa.')
    return

while True:
    num = []
    while True:
        n = int(input('Digite um número: '))
        num.append(n)
        r = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if r in 'N':
            break
    numero_maior(*num)
    r = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if r in 'N':
        break
print('Fim do programa.')
