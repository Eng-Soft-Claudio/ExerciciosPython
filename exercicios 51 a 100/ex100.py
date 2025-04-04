numeros = list()

def sortear():
    from random import randint
    for i in range(0, 5):
        numeros.append(randint(1, 10))
    print(f'Os números sorteados foram {numeros}')
    return

def somapar():
    soma = 0
    for i in numeros:
        if i % 2 == 0:
            soma += i
    print(f'A soma dos números pares é {soma}')
    return

sortear()
somapar()
