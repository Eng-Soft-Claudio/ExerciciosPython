from math import factorial

def fatorial(n, show=False):
    if show:
        for i in range(n, 0, -1):
            print(i, end='')
            if i > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        return factorial(n)
    else:
        return factorial(n)

n = int(input('Digite um número para calcular seu fatorial: '))
show = input('Deseja ver o cálculo? [S/N] ')
if show in 'Ss':
    print(fatorial(n, True))
else:
    print(fatorial(n))

