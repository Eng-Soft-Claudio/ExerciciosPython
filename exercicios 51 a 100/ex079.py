lista = []
while True:
    numero = (int(input("Digite um valor: ")))

    if numero not in lista:
        lista.append(numero)
        print("Valor adicionado com sucesso...")
    else:
        print("Valor duplicado. Não será adicionado...")

    continua = str(input("Deseja continuar? [S/N] ")).upper().strip()[0]
    if continua == "S":
        pass
    else:
        break
lista.sort()
print(f"Você digitou os valores: {lista}")