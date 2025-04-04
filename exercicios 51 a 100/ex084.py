lista_principal = []
lista_temporaria = []

maior = 0
menor = 0

while True:
    
    lista_temporaria.append(str(input("Nome: ")))
    lista_temporaria.append(float(input("Peso: ")))

    if len(lista_principal) == 0:
        maior = menor = lista_temporaria[1]
    else:
        if lista_temporaria[1] > maior:
            maior = lista_temporaria[1]
        if lista_temporaria[1] < menor:
            menor = lista_temporaria[1]

    lista_principal.append(lista_temporaria[:])
    lista_temporaria.clear()

    continua = str(input("Deseja continuar [S/N]: ")).upper().strip()[0]
    if continua == "N":
        break

print(f"Foram cadastradas {len(lista_principal)} pessoas.")
print("As pessoas mais pesadas são:", end="")
for pessoa in lista_principal:
    if pessoa[1] == maior:
        print(f"[{pessoa[0]}] ", end="")
print(f"\nAs pessoas mais leves são:", end="")
for pessoa in lista_principal:
    if pessoa[1] == menor:
        print(f"[{pessoa[0]}] ", end="")
