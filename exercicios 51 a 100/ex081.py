lista = []
while True:
    lista.append(int(input("Informe um valor: ")))
    lista.sort(reverse = True)
    continua = str(input("Deseja continuar [S/N]? ")).upper().strip()[0]
    if continua == "N":
        print(f"Foram digitados {len(lista)} valores.")
        print(f"Lista informada em ordem decrescente: {lista}")
        if 5 not in lista:
            print("O número 5 não foi informado para a lista.")
        else:
            print(f"O número 5 foi informado na lista.")
        break
        