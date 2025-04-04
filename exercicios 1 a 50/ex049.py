numero = int(input("Informe um número inteiro para ver a tabuada de multiplicação: "))
for n in range(1, 11):
    print(f"{numero} X {n:2} = {(numero * n):2}")