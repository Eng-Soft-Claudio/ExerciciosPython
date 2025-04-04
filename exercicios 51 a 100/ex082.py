lista_geral = []
lista_pares = []
lista_impares = []

print("=" * 40)

while True:

    lista_geral.append(int(input("Informe um número inteiro: ")))

    if lista_geral[-1] % 2 == 0:
        lista_pares.append(lista_geral[-1])
    else:
        lista_impares.append(lista_geral[-1])

    continua = str(input("Deseja continuar [S/N]: ")).upper().strip()[0]
    if continua == "N":
        print("=" * 40)
        print(f"Lista de todos os números: {lista_geral}")
        print(f"Lista dos números pares: {lista_pares}")
        print(f"Lista dos números ímpares: {lista_impares}")
        print("=" * 40)
        break
